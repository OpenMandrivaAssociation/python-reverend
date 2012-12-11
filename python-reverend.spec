%define oname Reverend

Summary: Python Bayesian classifier
Name:    python-reverend
Version: 0.3
Release: 8
Source:  http://prdownloads.sourceforge.net/%oname/%oname-%version.tar.bz2
License: GPL
Group: Development/Python
BuildRequires: python-devel
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
python setup.py install --root=%{buildroot}

%files 
%doc *.txt examples/
%py_puresitedir/reverend
%py_puresitedir/*egg-info




%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3-7mdv2010.0
+ Revision: 442481
- rebuild

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 0.3-6mdv2009.1
+ Revision: 324108
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.3-5mdv2009.0
+ Revision: 259775
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.3-4mdv2009.0
+ Revision: 247626
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.3-2mdv2008.1
+ Revision: 136460
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 16 2007 Michael Scherer <misc@mandriva.org> 0.3-2mdv2007.1
+ Revision: 144950
- fix build on x86_64
- rebuild for new python
- new project url
- Import python-reverend

* Sat Oct 22 2005 Michael Scherer <misc@mandriva.org> 0.3-1mdk
- initial release

