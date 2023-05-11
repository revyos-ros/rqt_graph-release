%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-rqt-graph
Version:        1.4.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rqt_graph package

License:        BSD
URL:            http://wiki.ros.org/rqt_graph
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-iron-ament-index-python
Requires:       ros-iron-python-qt-binding
Requires:       ros-iron-qt-dotgraph >= 1.1.2
Requires:       ros-iron-rqt-gui
Requires:       ros-iron-rqt-gui-py
Requires:       ros-iron-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
rqt_graph provides a GUI plugin for visualizing the ROS computation graph. Its
components are made generic so that other packages where you want to achieve
graph representation can depend upon this pkg (use rqt_dep to find out the pkgs
that depend. rqt_dep itself depends on rqt_graph too).

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/iron"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Thu May 11 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.4.2-1
- Autogenerated by Bloom

* Thu Apr 20 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.4.1-3
- Autogenerated by Bloom

* Tue Mar 21 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.4.1-2
- Autogenerated by Bloom
