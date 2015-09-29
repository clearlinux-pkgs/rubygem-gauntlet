#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-gauntlet
Version  : 2.1.0
Release  : 8
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
/usr/lib64/ruby/gems/2.2.0/cache/gauntlet-2.1.0.gem
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Array/average-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Array/cdesc-Array.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Array/sample_variance-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Array/stddev-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Array/sum-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/cdesc-Gauntlet.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/data-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/data_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/dirty-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/each_gem-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/in_gem_dir-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/initialize_dir-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/latest_gems-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/load_yaml-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/run_the_gauntlet-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/save_yaml-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/should_skip%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/shutdown-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/source_index-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/update_gem_tarballs-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/with_gem-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gauntlet/workers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gem/SpecFetcher/cdesc-SpecFetcher.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gem/SpecFetcher/fetcher-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gem/SpecFetcher/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gem/SpecFetcher/old_initialize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/Gem/cdesc-Gem.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/GrepGauntlet/args-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/GrepGauntlet/cdesc-GrepGauntlet.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/GrepGauntlet/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/GrepGauntlet/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/page-History_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/page-Manifest_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/gauntlet-2.1.0/ri/page-README_txt.ri
/usr/lib64/ruby/gems/2.2.0/gems/gauntlet-2.1.0/.gemtest
/usr/lib64/ruby/gems/2.2.0/gems/gauntlet-2.1.0/History.txt
/usr/lib64/ruby/gems/2.2.0/gems/gauntlet-2.1.0/Manifest.txt
/usr/lib64/ruby/gems/2.2.0/gems/gauntlet-2.1.0/README.txt
/usr/lib64/ruby/gems/2.2.0/gems/gauntlet-2.1.0/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/gauntlet-2.1.0/bin/gauntlet
/usr/lib64/ruby/gems/2.2.0/gems/gauntlet-2.1.0/lib/gauntlet.rb
/usr/lib64/ruby/gems/2.2.0/gems/gauntlet-2.1.0/lib/gauntlet_grep.rb
/usr/lib64/ruby/gems/2.2.0/gems/gauntlet-2.1.0/test/test_gauntlet.rb
/usr/lib64/ruby/gems/2.2.0/specifications/gauntlet-2.1.0.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/gauntlet
