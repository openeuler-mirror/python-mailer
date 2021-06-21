%global _empty_manifest_terminate_build 0
Name:		python-mailer
Version:	0.8.1
Release:	1
Summary:	A module to send email simply in Python
License:	MIT
URL:		https://bitbucket.org/ginstrom/mailer
Source0:	https://files.pythonhosted.org/packages/30/e7/c3a932fc03ab95c96ff911d8ee3e89b937205596a5c1f00849401a2468e0/mailer-0.8.1.zip
BuildArch:	noarch
%description
Here are some of the features:

* Single class to send plain text, HTML email, and attachments
* Auto detects attachment types
* Support for internationalized headers

Changes in version 0.3
----------------------

The API for Mailer.To is changed. Use a string to specify a single recipient,
and an iterable to specify more than one.

Changes in version 0.4
----------------------

You can now specify the port in Mailer ::

 from mailer import Mailer
 sender = Mailer('smtp.example.com', port=20)

Changes in version 0.5
----------------------

* Message.attach takes an optional cid argument.
* You can now send HTML emails with attachments

Thanks to Douglas Mayle for his patch for this.

Changes in version 0.6
----------------------

* Can now select port
* Supports gmail

Changes in version 0.7
----------------------

* You can now specify MIME type::

    msg.attach("picture.png", mimetype="image/png")

Changes in version 0.8
----------------------

* Various bug fixes

Examples
------------------

**Sending an HTML email:** ::

 from mailer import Mailer
 from mailer import Message
 
 message = Message(From="me@example.com",
                   To="you@example.com",
                   charset="utf-8")
 message.Subject = "An HTML Email"
 message.Html = """This email uses <strong>HTML</strong>!"""
 message.Body = """This is alternate text."""
 
 sender = Mailer('smtp.example.com')
 sender.send(message)

**Sending an attachment:** ::

 from mailer import Mailer
 from mailer import Message
 
 message = Message(From="me@example.com",
                   To=["you@example.com", "him@example.com"],
                   Subject="Cute Cat")
 message.Body = """Kittens with dynamite"""
 message.attach("kitty.jpg")

 sender = Mailer('smtp.example.com')
 sender.send(message)

Tested with Python 2.4, 2.5, and 2.6

%package -n python3-mailer
Summary:	A module to send email simply in Python
Provides:	python-mailer
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pbr
%description -n python3-mailer
Here are some of the features:

* Single class to send plain text, HTML email, and attachments
* Auto detects attachment types
* Support for internationalized headers

Changes in version 0.3
----------------------

The API for Mailer.To is changed. Use a string to specify a single recipient,
and an iterable to specify more than one.

Changes in version 0.4
----------------------

You can now specify the port in Mailer ::

 from mailer import Mailer
 sender = Mailer('smtp.example.com', port=20)

Changes in version 0.5
----------------------

* Message.attach takes an optional cid argument.
* You can now send HTML emails with attachments

Thanks to Douglas Mayle for his patch for this.

Changes in version 0.6
----------------------

* Can now select port
* Supports gmail

Changes in version 0.7
----------------------

* You can now specify MIME type::

    msg.attach("picture.png", mimetype="image/png")

Changes in version 0.8
----------------------

* Various bug fixes

Examples
------------------

**Sending an HTML email:** ::

 from mailer import Mailer
 from mailer import Message
 
 message = Message(From="me@example.com",
                   To="you@example.com",
                   charset="utf-8")
 message.Subject = "An HTML Email"
 message.Html = """This email uses <strong>HTML</strong>!"""
 message.Body = """This is alternate text."""
 
 sender = Mailer('smtp.example.com')
 sender.send(message)

**Sending an attachment:** ::

 from mailer import Mailer
 from mailer import Message
 
 message = Message(From="me@example.com",
                   To=["you@example.com", "him@example.com"],
                   Subject="Cute Cat")
 message.Body = """Kittens with dynamite"""
 message.attach("kitty.jpg")

 sender = Mailer('smtp.example.com')
 sender.send(message)

Tested with Python 2.4, 2.5, and 2.6

%package help
Summary:	Development documents and examples for mailer
Provides:	python3-mailer-doc
%description help
Here are some of the features:

* Single class to send plain text, HTML email, and attachments
* Auto detects attachment types
* Support for internationalized headers

Changes in version 0.3
----------------------

The API for Mailer.To is changed. Use a string to specify a single recipient,
and an iterable to specify more than one.

Changes in version 0.4
----------------------

You can now specify the port in Mailer ::

 from mailer import Mailer
 sender = Mailer('smtp.example.com', port=20)

Changes in version 0.5
----------------------

* Message.attach takes an optional cid argument.
* You can now send HTML emails with attachments

Thanks to Douglas Mayle for his patch for this.

Changes in version 0.6
----------------------

* Can now select port
* Supports gmail

Changes in version 0.7
----------------------

* You can now specify MIME type::

    msg.attach("picture.png", mimetype="image/png")

Changes in version 0.8
----------------------

* Various bug fixes

Examples
------------------

**Sending an HTML email:** ::

 from mailer import Mailer
 from mailer import Message
 
 message = Message(From="me@example.com",
                   To="you@example.com",
                   charset="utf-8")
 message.Subject = "An HTML Email"
 message.Html = """This email uses <strong>HTML</strong>!"""
 message.Body = """This is alternate text."""
 
 sender = Mailer('smtp.example.com')
 sender.send(message)

**Sending an attachment:** ::

 from mailer import Mailer
 from mailer import Message
 
 message = Message(From="me@example.com",
                   To=["you@example.com", "him@example.com"],
                   Subject="Cute Cat")
 message.Body = """Kittens with dynamite"""
 message.attach("kitty.jpg")

 sender = Mailer('smtp.example.com')
 sender.send(message)

Tested with Python 2.4, 2.5, and 2.6

%prep
%autosetup -n mailer-0.8.1

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-mailer -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Thu Jun 17 2021 OpenStack_SIG <openstack@openeuler.org>
- Package Spec generated
