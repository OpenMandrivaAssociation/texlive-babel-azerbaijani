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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the babel style for Azerbaijani. This language poses special
challenges because no "traditional" font encoding contains the full
character set, and therefore a mixture must be used (e.g., T2A and T1).
This package is compatible with Unicode engines (LuaTeX, XeTeX), which
are very likely the most convenient way to write Azerbaijani documents.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-azerbaijani
%dir %{_datadir}/texmf-dist/source/generic/babel-azerbaijani
%dir %{_datadir}/texmf-dist/tex/generic/babel-azerbaijani
%doc %{_datadir}/texmf-dist/doc/generic/babel-azerbaijani/README
%doc %{_datadir}/texmf-dist/doc/generic/babel-azerbaijani/azerbaijani.pdf
%doc %{_datadir}/texmf-dist/source/generic/babel-azerbaijani/azerbaijani.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-azerbaijani/azerbaijani.ins
%{_datadir}/texmf-dist/tex/generic/babel-azerbaijani/azerbaijani.ldf
