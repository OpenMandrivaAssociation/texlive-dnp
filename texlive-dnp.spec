%global tl_name dnp
%global tl_revision 54074

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	subfont numbers for DNP font encoding
Group:		Publishing
URL:		https://www.ctan.org/pkg/dnp
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dnp.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
part of the CJK package, ctan.org/pkg/cjk

