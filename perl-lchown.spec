%include	/usr/lib/rpm/macros.perl

Summary:	Lchown - use the lchown(2) system call from Perl
Name:		perl-lchown
Version:	1.01
Release:	1
# same as perl
License:	GPL v1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/N/NC/NCLEATON/Lchown-%{version}.tar.gz
# Source0-md5:	e3db31be650437eb5d9bfc4da6252ee3
URL:		https://metacpan.org/release/Lchown
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lchown - use the lchown(2) system call from Perl.

%prep
%setup -qn Lchown-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/auto/Lchown
%attr(755,root,root) %{perl_vendorarch}/auto/Lchown/Lchown.so
%{perl_vendorarch}/auto/Lchown/Lchown.bs
%{perl_vendorarch}/Lchown.pm
%{_mandir}/man3/*

