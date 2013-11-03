#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
Summary:	Parse cpanfile
Name:		perl-Module-CPANfile
Version:	1.0001
Release:	1
License:	GPL+ or Artistic
Group:		Development/Libraries
Source0:	http://www.cpan.org/authors/id/M/MI/MIYAGAWA/Module-CPANfile-%{version}.tar.gz
# Source0-md5:	d1fa25121f0409182a21b2ef89ab58e0
URL:		http://search.cpan.org/dist/Module-CPANfile/
BuildRequires:	perl(CPAN::Meta) >= 2.12091
BuildRequires:	perl(CPAN::Meta::Feature) >= 2.12091
BuildRequires:	perl(CPAN::Meta::Prereqs) >= 2.12091
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:	perl(base)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl-Encode
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Exporter)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Test::More) >= 0.88
%endif
Requires:	perl(CPAN::Meta) >= 2.12091
Requires:	perl(CPAN::Meta::Feature) >= 2.12091
Requires:	perl(CPAN::Meta::Prereqs) >= 2.12091
Requires:	perl(Data::Dumper)
Requires:	perl(Pod::Usage)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::CPANfile is a tool to handle cpanfile format to load
application specific dependencies, not just for CPAN distributions.

%prep
%setup -q -n Module-CPANfile-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Module/CPANfile/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%attr(755,root,root) %{_bindir}/mymeta-cpanfile
%{_mandir}/man1/mymeta-cpanfile*
%{_mandir}/man3/Module::CPANfile.3pm*
%{_mandir}/man3/cpanfile-faq.3pm*
%{_mandir}/man3/cpanfile.3pm*
%{perl_vendorlib}/Module/CPANfile.pm
%{perl_vendorlib}/Module/CPANfile
%{perl_vendorlib}/cpanfile-faq.pod
%{perl_vendorlib}/cpanfile.pod
