Name:		texlive-ijsra
Version:	44886
Release:	1
Summary:	LaTeX document class for the International Journal of Student Research in Archaeology
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ijsra
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ijsra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ijsra.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a document class called ijsra which is used for the
International Journal of Student Research in Archaeology.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ijsra
%doc %{_texmfdistdir}/doc/latex/ijsra

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
