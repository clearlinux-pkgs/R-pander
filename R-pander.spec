#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-pander
Version  : 0.6.6
Release  : 28
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/pander_0.6.6.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/pander_0.6.6.tar.gz
Summary  : An R 'Pandoc' Writer
Group    : Development/Tools
License  : AGPL-3.0 OSL-3.0
Requires: R-pander-lib = %{version}-%{release}
Requires: R-pander-license = %{version}-%{release}
Requires: R-Rcpp
Requires: R-digest
BuildRequires : R-Rcpp
BuildRequires : R-digest
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
useful information while evaluating R code and other helpers to return user

%package lib
Summary: lib components for the R-pander package.
Group: Libraries
Requires: R-pander-license = %{version}-%{release}

%description lib
lib components for the R-pander package.


%package license
Summary: license components for the R-pander package.
Group: Default

%description license
license components for the R-pander package.


%prep
%setup -q -n pander
pushd ..
cp -a pander buildavx2
popd
pushd ..
cp -a pander buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742476638

%install
export SOURCE_DATE_EPOCH=1742476638
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-pander
cp %{_builddir}/pander/LICENSE %{buildroot}/usr/share/package-licenses/R-pander/02ed0c61f33ebae1d96ce93601ff149311eaabdb || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pander/DESCRIPTION
/usr/lib64/R/library/pander/INDEX
/usr/lib64/R/library/pander/LICENSE
/usr/lib64/R/library/pander/Meta/Rd.rds
/usr/lib64/R/library/pander/Meta/features.rds
/usr/lib64/R/library/pander/Meta/hsearch.rds
/usr/lib64/R/library/pander/Meta/links.rds
/usr/lib64/R/library/pander/Meta/nsInfo.rds
/usr/lib64/R/library/pander/Meta/package.rds
/usr/lib64/R/library/pander/Meta/vignette.rds
/usr/lib64/R/library/pander/NAMESPACE
/usr/lib64/R/library/pander/NEWS.md
/usr/lib64/R/library/pander/R/pander
/usr/lib64/R/library/pander/R/pander.rdb
/usr/lib64/R/library/pander/R/pander.rdx
/usr/lib64/R/library/pander/README.brew
/usr/lib64/R/library/pander/doc/evals.R
/usr/lib64/R/library/pander/doc/evals.Rmd
/usr/lib64/R/library/pander/doc/evals.html
/usr/lib64/R/library/pander/doc/index.html
/usr/lib64/R/library/pander/doc/knitr.R
/usr/lib64/R/library/pander/doc/knitr.Rmd
/usr/lib64/R/library/pander/doc/knitr.html
/usr/lib64/R/library/pander/doc/pander.R
/usr/lib64/R/library/pander/doc/pander.Rmd
/usr/lib64/R/library/pander/doc/pander.html
/usr/lib64/R/library/pander/doc/pandoc_table.R
/usr/lib64/R/library/pander/doc/pandoc_table.Rmd
/usr/lib64/R/library/pander/doc/pandoc_table.html
/usr/lib64/R/library/pander/examples/graphs.brew
/usr/lib64/R/library/pander/examples/minimal.brew
/usr/lib64/R/library/pander/examples/olympics.brew
/usr/lib64/R/library/pander/examples/short-code-long-report.brew
/usr/lib64/R/library/pander/flycheck_pander.elc
/usr/lib64/R/library/pander/help/AnIndex
/usr/lib64/R/library/pander/help/aliases.rds
/usr/lib64/R/library/pander/help/pander.rdb
/usr/lib64/R/library/pander/help/pander.rdx
/usr/lib64/R/library/pander/help/paths.rds
/usr/lib64/R/library/pander/html/00Index.html
/usr/lib64/R/library/pander/html/R.css
/usr/lib64/R/library/pander/includes/html/footer.html
/usr/lib64/R/library/pander/includes/html/header.html
/usr/lib64/R/library/pander/includes/images/apple-touch-icon-114x114.png
/usr/lib64/R/library/pander/includes/images/apple-touch-icon-72x72.png
/usr/lib64/R/library/pander/includes/images/apple-touch-icon.png
/usr/lib64/R/library/pander/includes/images/closelabel.gif
/usr/lib64/R/library/pander/includes/images/favicon.gif
/usr/lib64/R/library/pander/includes/images/loading.gif
/usr/lib64/R/library/pander/includes/images/logo.png
/usr/lib64/R/library/pander/includes/images/nextlabel.gif
/usr/lib64/R/library/pander/includes/images/prevlabel.gif
/usr/lib64/R/library/pander/includes/javascripts/custom.js
/usr/lib64/R/library/pander/includes/javascripts/jcaption.min.js
/usr/lib64/R/library/pander/includes/javascripts/jquery-1.7.2.min.js
/usr/lib64/R/library/pander/includes/javascripts/slimbox2.js
/usr/lib64/R/library/pander/includes/javascripts/tabs.js
/usr/lib64/R/library/pander/includes/stylesheets/base.css
/usr/lib64/R/library/pander/includes/stylesheets/caption.css
/usr/lib64/R/library/pander/includes/stylesheets/custom.css
/usr/lib64/R/library/pander/includes/stylesheets/layout.css
/usr/lib64/R/library/pander/includes/stylesheets/skeleton.css
/usr/lib64/R/library/pander/includes/stylesheets/slimbox2.css
/usr/lib64/R/library/pander/pander.el
/usr/lib64/R/library/pander/tests/test-R5.R
/usr/lib64/R/library/pander/tests/test-S3.R
/usr/lib64/R/library/pander/tests/test-brew.R
/usr/lib64/R/library/pander/tests/test-convert.R
/usr/lib64/R/library/pander/tests/test-evals.R
/usr/lib64/R/library/pander/tests/test-helpers.R
/usr/lib64/R/library/pander/tests/test-missing.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/pander/libs/pander.so
/V4/usr/lib64/R/library/pander/libs/pander.so
/usr/lib64/R/library/pander/libs/pander.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-pander/02ed0c61f33ebae1d96ce93601ff149311eaabdb
