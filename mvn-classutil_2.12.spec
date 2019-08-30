#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-classutil_2.12
Version  : 1.1.2
Release  : 2
URL      : https://github.com/bmc/classutil/archive/release-1.1.2.tar.gz
Source0  : https://github.com/bmc/classutil/archive/release-1.1.2.tar.gz
Source1  : https://repo1.maven.org/maven2/org/clapper/classutil_2.12/1.1.2/classutil_2.12-1.1.2.jar
Source2  : https://repo1.maven.org/maven2/org/clapper/classutil_2.12/1.1.2/classutil_2.12-1.1.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-classutil_2.12-data = %{version}-%{release}

%description
classutil: Fast class finder utilities, plus some extras
========================================================

%package data
Summary: data components for the mvn-classutil_2.12 package.
Group: Data

%description data
data components for the mvn-classutil_2.12 package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/clapper/classutil_2.12/1.1.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/clapper/classutil_2.12/1.1.2/classutil_2.12-1.1.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/clapper/classutil_2.12/1.1.2
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/clapper/classutil_2.12/1.1.2/classutil_2.12-1.1.2.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/clapper/classutil_2.12/1.1.2/classutil_2.12-1.1.2.jar
/usr/share/java/.m2/repository/org/clapper/classutil_2.12/1.1.2/classutil_2.12-1.1.2.pom
