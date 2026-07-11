%global tl_name babel-azerbaijani
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0a
Release:	%{tl_revision}.1
Summary:	Support for Azerbaijani within babel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/azerbaijani
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-azerbaijani.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-azerbaijani.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-azerbaijani.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the babel style for Azerbaijani. This language poses special
challenges because no "traditional" font encoding contains the full
character set, and therefore a mixture must be used (e.g., T2A and T1).
This package is compatible with Unicode engines (LuaTeX, XeTeX), which
are very likely the most convenient way to write Azerbaijani documents.

