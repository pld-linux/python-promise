#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Promises/A+ implementation for Python
Summary(pl.UTF-8):	Implementacja Promises/A+ dla Pythona
Name:		python-promise
Version:	2.3
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/promise/
Source0:	https://files.pythonhosted.org/packages/source/p/promise/promise-%{version}.tar.gz
# Source0-md5:	28a14b6bcf3bd7d351cb158621600faf
URL:		https://pypi.org/project/promise/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-futures
BuildRequires:	python-mock
BuildRequires:	python-pytest >= 2.7.3
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-futures
BuildRequires:	python3-pytest >= 2.7.3
BuildRequires:	python3-pytest-asyncio
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a implementation of Promises in Python. It is a super set of
Promises/A+ designed to have readable, performant code and to provide
just the extensions that are absolutely necessary for using promises
in Python.

%description -l pl.UTF-8
Implementacja obietnic w Pythonie. Jest to nadzbiór Promises/A+
zaprojektowany z myślą o czytelnym, wydajnym kodzie; dostarcza tylko
te rozszerzenia, które są całkowicie niezbędne do używania obietnic w
Pythonie.

%package -n python3-promise
Summary:	Promises/A+ implementation for Python
Summary(pl.UTF-8):	Implementacja Promises/A+ dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-promise
This is a implementation of Promises in Python. It is a super set of
Promises/A+ designed to have readable, performant code and to provide
just the extensions that are absolutely necessary for using promises
in Python.

%description -n python3-promise -l pl.UTF-8
Implementacja obietnic w Pythonie. Jest to nadzbiór Promises/A+
zaprojektowany z myślą o czytelnym, wydajnym kodzie; dostarcza tylko
te rozszerzenia, które są całkowicie niezbędne do używania obietnic w
Pythonie.

%prep
%setup -q -n promise-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/promise
%{py_sitescriptdir}/promise-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-promise
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/promise
%{py3_sitescriptdir}/promise-%{version}-py*.egg-info
%endif
