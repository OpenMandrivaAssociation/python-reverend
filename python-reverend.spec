%define name python-reverend
%define version 0.3
%define release %mkrel 4
%define oname Reverend

Summary: Python Bayesian classifier
Name: %{name}
Version: %{version}
Release: %{release}
Source:  http://prdownloads.sourceforge.net/%oname/%oname-%version.tar.bz2
License: GPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libpython-devel
Url: http://divmod.org/trac/wiki/DivmodReverend 
BuildArch: noarch

%description
Reverend is a general purpose Bayesian classifier, named after Rev. Thomas 
Bayes. Use the Reverend to quickly add Bayesian smarts to your app.
 
To use it in your own application, you either subclass Bayes or pass it a 
tokenizing function. Bayesian fun has never been so quick and easy. 

%prep
%setup -q -n %oname-%version 

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc *.txt examples/
%py_puresitedir/reverend
%py_puresitedir/*egg-info


