#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-gauntlet
Version  : 2.1.0
Release  : 10
URL      : https://rubygems.org/downloads/gauntlet-2.1.0.gem
Source0  : https://rubygems.org/downloads/gauntlet-2.1.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-gauntlet-bin
BuildRequires : ruby
BuildRequires : rubygem-hoe
BuildRequires : rubygem-net-http-persistent
BuildRequires : rubygem-rdoc

%description
= gauntlet
home :: https://github.com/seattlerb/gauntlet
== DESCRIPTION:
Gauntlet is a pluggable means of running code against all the latest
gems and storing off the data.

%package bin
Summary: bin components for the rubygem-gauntlet package.
Group: Binaries

%description bin
bin components for the rubygem-gauntlet package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n gauntlet-2.1.0
gem spec %{SOURCE0} -l --ruby > rubygem-gauntlet.gemspec

%build
gem build rubygem-gauntlet.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
gauntlet-2.1.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/gauntlet-2.1.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/gauntlet-2.1.0/.gemtest
/usr/lib64/ruby/gems/2.3.0/gems/gauntlet-2.1.0/History.txt
/usr/lib64/ruby/gems/2.3.0/gems/gauntlet-2.1.0/Manifest.txt
/usr/lib64/ruby/gems/2.3.0/gems/gauntlet-2.1.0/README.txt
/usr/lib64/ruby/gems/2.3.0/gems/gauntlet-2.1.0/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/gauntlet-2.1.0/bin/gauntlet
/usr/lib64/ruby/gems/2.3.0/gems/gauntlet-2.1.0/lib/gauntlet.rb
/usr/lib64/ruby/gems/2.3.0/gems/gauntlet-2.1.0/lib/gauntlet_grep.rb
/usr/lib64/ruby/gems/2.3.0/gems/gauntlet-2.1.0/test/test_gauntlet.rb
/usr/lib64/ruby/gems/2.3.0/specifications/gauntlet-2.1.0.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/gauntlet
