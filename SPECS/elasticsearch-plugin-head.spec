%define debug_package %{nil}
%define base_install_dir %{_javadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-head
Version:        1.0.0
Release:        1%{?dist}
Summary:        ElasticSearch administrative web interface

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/mobz/elasticsearch-head

Source0:        https://github.com/mobz/elasticsearch-head/archive/master.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.19.9

%description
Provides an administrative web interface for elasticsearch

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/head

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}

%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins/head
%{__cp} -r plugins/head/elasticsearch-head-master %{buildroot}/%{base_install_dir}/plugins/head/_site

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/head
%{base_install_dir}/plugins/head/*

%changelog
* Tue Mar 12 2013 Blake Smith 1.0
- Initial package
