%global tl_name ijsra
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	LaTeX document class for the International Journal of Student Research in Arc...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ijsra
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ijsra.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ijsra.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a document class called ijsra which is used for the
International Journal of Student Research in Archaeology.

