Name:		texlive-babel-azerbaijani
Version:	44197
Release:	2
Summary:	Support for Azerbaijani within babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-azerbaijani
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-azerbaijani.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-azerbaijani.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-azerbaijani.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is the babel style for Azerbaijani. This language poses
special challenges because no "traditional" font encoding
contains the full character set, and therefore a mixture must
be used (e.g., T2A and T1). This package is compatible with
Unicode engines (LuaTeX, XeTeX), which are very likely the most
convenient way to write Azerbaijani documents.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/babel-azerbaijani
%{_texmfdistdir}/tex/generic/babel-azerbaijani
%doc %{_texmfdistdir}/doc/generic/babel-azerbaijani

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
