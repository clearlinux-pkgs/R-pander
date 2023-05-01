#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pander
Version  : 0.6.5
Release  : 22
URL      : https://cran.r-project.org/src/contrib/pander_0.6.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pander_0.6.5.tar.gz
Summary  : An R 'Pandoc' Writer
Group    : Development/Tools
License  : AGPL-3.0 OSL-3.0
Requires: R-pander-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-digest
BuildRequires : R-Rcpp
BuildRequires : R-digest
BuildRequires : buildreq-R

%description
useful information while evaluating R code and other helpers to return user

%package lib
Summary: lib components for the R-pander package.
Group: Libraries

%description lib
lib components for the R-pander package.


%prep
%setup -q -c -n pander
cd %{_builddir}/pander

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647620254

%install
export SOURCE_DATE_EPOCH=1647620254
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pander
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pander
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pander
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pander || :


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
/usr/lib64/R/library/pander/NEWS
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
/usr/lib64/R/library/pander/libs/pander.so
/usr/lib64/R/library/pander/libs/pander.so.avx2
/usr/lib64/R/library/pander/libs/pander.so.avx512
