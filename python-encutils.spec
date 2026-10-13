Name:		python-encutils
Version:	1.0.0
Release:	2
Summary:	Encoding detection helpers split out of cssutils
License:	LGPL-3.0-or-later
Group:		Development/Python
URL:		https://pypi.org/project/encutils/
Source0:	encutils-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(chardet)
BuildArch:	noarch
%description
Encoding detection helpers used by cssutils.

%files
%{py_sitedir}/*
