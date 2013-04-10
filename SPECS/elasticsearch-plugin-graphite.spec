%define debug_package %{nil}
%define base_install_dir %{_javadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-graphite
Version:        0.2
Release:        2%{?dist}
Summary:        ElasticSearch plugin to push statistics to graphite

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/spinscale/elasticsearch-graphite-plugin

Source0:        file:///path/to/local/file/elasticsearch-plugin-graphite-0.2.jar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.19

%description
ElasticSearch plugin to push statistics to graphite

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins/graphite
cp %{SOURCE0} plugins/graphite

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__install} -D -m 755 plugins/graphite/elasticsearch-plugin-graphite-%{version}.jar %{buildroot}/%{base_install_dir}/plugins/graphite/elasticsearch-plugin-graphite.jar

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/graphite
%{base_install_dir}/plugins/graphite/*

%changelog
* Tue Apr 9 2013 Blake Smith 0.2
- Initial package

