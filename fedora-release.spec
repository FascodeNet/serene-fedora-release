%define release_name Rawhide

Summary:	Fedora release files
Name:		fedora-release
Version:	7
Release:	1
License:	GFDL
Group:		System Environment/Base
URL:		http://fedoraproject.org
Source:		%{name}-%{version}.tar.gz
Obsoletes:	redhat-release
Provides:	redhat-release
Requires:	fedora-release-notes >= 6
# We require release notes to make sure that they don't get dropped during
# upgrades, and just because we always want the release notes available
# instead of explicitly asked for
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
Fedora release files such as yum configs and various /etc/ files that
define the release.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc
echo "Fedora release %{version} (%{release_name})" > $RPM_BUILD_ROOT/etc/fedora-release
cp -p $RPM_BUILD_ROOT/etc/fedora-release $RPM_BUILD_ROOT/etc/issue
echo "Kernel \r on an \m" >> $RPM_BUILD_ROOT/etc/issue
cp -p $RPM_BUILD_ROOT/etc/issue $RPM_BUILD_ROOT/etc/issue.net
echo >> $RPM_BUILD_ROOT/etc/issue
ln -s fedora-release $RPM_BUILD_ROOT/etc/redhat-release

install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
for file in RPM-GPG-KEY* ; do
	install -m 644 $file $RPM_BUILD_ROOT/etc/pki/rpm-gpg
done

install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
for file in fedora*repo ; do
  install -m 644 $file $RPM_BUILD_ROOT/etc/yum.repos.d
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%attr(0644,root,root) /etc/fedora-release
/etc/redhat-release
%dir /etc/yum.repos.d
%config(noreplace) /etc/yum.repos.d/*
%doc GPL 
%config(noreplace) %attr(0644,root,root) /etc/issue
%config(noreplace) %attr(0644,root,root) /etc/issue.net
%dir /etc/pki/rpm-gpg
/etc/pki/rpm-gpg/*

%changelog
* Mon May 21 2007 Jesse Keating <jkeating@redhat.com> - 7-1
- First build for Fedora 7
- Remove Extras repos (YAY!)
- Remove references to "core" in repo files.
- Adjust repo files for new mirror structure
- Remove Legacy repo

* Fri Apr 20 2007 Jesse Keating <jkeating@redhat.com> - 6.93-1
- Bump for Test 4

* Mon Mar 19 2007 Jesse Keating <jkeating@redhat.com> - 6.92-1
- Bump for Test 3
- No more eula in fedora-release, moved to firstboot

* Fri Feb 23 2007 Jesse Keating <jkeating@redhat.com> - 6.91-1
- Bump for Test 2

* Tue Feb 13 2007 Jesse Keating <jkeating@redhat.com> - 6.90-4
- Specfile cleanups

* Mon Feb 05 2007 Jesse Keating <jkeating@redhat.com> - 6.90-3
- Drop the legacy repo file.

* Fri Jan 26 2007 Jesse Keating <jkeating@redhat.com> - 6.90-2
- Core?  What Core?

* Wed Jan 24 2007 Jeremy Katz <katzj@redhat.com> - 6.90-1
- Bump to 6.90.  Keep working with older release notes

* Mon Oct 16 2006 Jesse Keating <jkeating@redhat.com> - 6-89
- Keep version 6, bump release.  Saves from having to rebuild
  release notes all the time

* Sun Oct 15 2006 Jesse Keating <jkeating@redhat.com> - 6.89-1
- Rebuild for rawhide

* Thu Oct 12 2006 Jesse Keating <jkeating@redhat.com> - 6-3
- version has to stay the same, safe to use.

* Thu Oct  5 2006 Jesse Keating <jkeating@redhat.com> - 6-2
- replace old mirror files with new mirrorlist cgi system

* Thu Oct  5 2006 Jesse Keating <jkeating@redhat.com> - 6-1
- Rebuild for Fedora Core 6 release

* Tue Sep  5 2006 Jesse Keating <jkeating@redhat.com> - 5.92-1
- Bump for FC6 Test3

* Thu Jul 27 2006 Jesse Keating <jkeating@redhat.com> - 5.91.1-1
- Convert deprecated gtk calls. (#200242)
- Fix some of the versioning

* Sun Jul 23 2006 Jesse Keating <jkeating@redhat.com> - 5.91-4
- Bump for FC6 Test2
- Remove release-notes content, now standalone package
- Don't replace issue and issue.net if the end user has modified it
- Require fedora-release-notes
- Cleanups

* Mon Jun 19 2006 Jesse Keating <jkeating@redhat.com> - 5.90-3
- Cleanups

* Thu Jun 15 2006 Jesse Keating <jkeating@redhat.com> - 5.90-1
- Update for 5.90

* Wed May 24 2006 Jesse Keating <jkeating@redhat.com> - 5.89-rawhide.2
- Update to get new devel repo file
- merge minor changes from external cvs .spec file

* Wed Apr 19 2006 Jesse Keating <jkeating@redhat.com> - 5.89-rawhide.1
- Look, a changelog!
- Removed duplicate html/css content from doc dir.
- Add lynx as a buildreq

