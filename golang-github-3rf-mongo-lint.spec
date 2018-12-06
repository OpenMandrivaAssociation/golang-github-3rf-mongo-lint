# https://github.com/3rf/mongo-lint
%global goipath         github.com/3rf/mongo-lint
%global commit          f6cf4f8a7d07167375b035d186a1e8b3ebf28aa3

%gometa

Name:           %{goname}
Version:        0
Release:        0.15%{?dist}
Summary:        MongoDB fork of Golint
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
%gochecks -d .

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README

%changelog
* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.15.20140702gitf6cf4f8
- SPEC refresh

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gitf6cf4f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.gitf6cf4f8
- Upload glide.lock and glide.yaml files

* Mon Mar 05 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.gitf6cf4f8
- Update to spec 3.0

* Mon Feb 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.20140702gitf6cf4f8
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitf6cf4f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitf6cf4f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitf6cf4f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitf6cf4f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 jchaloup <jchaloup@redhat.com> - 0-0.6.gitf6cf4f8
- Enable devel and unit-test for epel7
  resolves: #1365216

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.gitf6cf4f8
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gitf6cf4f8
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitf6cf4f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 jchaloup <jchaloup@redhat.com> - 0-0.2.gitf6cf4f8
- although testdata contains go files it is used only for testing purposes
  related: #1301568

* Mon Jan 25 2016 Marek Skalický <mskalick@redhat.com> - 0-0.1.gitf6cf4f8
- First package for Fedora
  resolves: #1301568
