#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : salib
Version  : 1.4.5
Release  : 4
URL      : https://files.pythonhosted.org/packages/c9/eb/d99fc629b5c40c79231027879bdba738d28b182335a6ff05ea0b8a2b7f38/SALib-1.4.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/c9/eb/d99fc629b5c40c79231027879bdba738d28b182335a6ff05ea0b8a2b7f38/SALib-1.4.5.tar.gz
Summary  : Tools for sensitivity analysis. Contains Sobol, Morris, and FAST methods
Group    : Development/Tools
License  : MIT
Requires: salib-bin = %{version}-%{release}
Requires: salib-license = %{version}-%{release}
Requires: salib-python = %{version}-%{release}
Requires: salib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(matplotlib)
BuildRequires : pypi(numpy)
BuildRequires : pypi(pandas)
BuildRequires : pypi(pathos)
BuildRequires : pypi(scipy)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Sensitivity Analysis Library (SALib)
====================================
Python implementations of commonly used sensitivity analysis methods.
Useful in systems modeling to calculate the effects of model inputs or
exogenous factors on outputs of interest.

%package bin
Summary: bin components for the salib package.
Group: Binaries
Requires: salib-license = %{version}-%{release}

%description bin
bin components for the salib package.


%package license
Summary: license components for the salib package.
Group: Default

%description license
license components for the salib package.


%package python
Summary: python components for the salib package.
Group: Default
Requires: salib-python3 = %{version}-%{release}

%description python
python components for the salib package.


%package python3
Summary: python3 components for the salib package.
Group: Default
Requires: python3-core
Provides: pypi(salib)
Requires: pypi(matplotlib)
Requires: pypi(numpy)
Requires: pypi(pandas)
Requires: pypi(pathos)
Requires: pypi(scipy)
Requires: pypi(setuptools)
Requires: pypi(wheel)

%description python3
python3 components for the salib package.


%prep
%setup -q -n SALib-1.4.5
cd %{_builddir}/SALib-1.4.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638315260
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/salib
cp %{_builddir}/SALib-1.4.5/LICENSE.txt %{buildroot}/usr/share/package-licenses/salib/ec29ae7be91d88e81a156aadae721a2b974efd9a
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/salib
/usr/bin/salib.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/salib/ec29ae7be91d88e81a156aadae721a2b974efd9a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
