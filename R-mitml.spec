#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mitml
Version  : 0.4.5
Release  : 16
URL      : https://cran.r-project.org/src/contrib/mitml_0.4-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mitml_0.4-5.tar.gz
Summary  : Tools for Multiple Imputation in Multilevel Modeling
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-haven
Requires: R-jomo
Requires: R-pan
BuildRequires : R-haven
BuildRequires : R-jomo
BuildRequires : R-pan
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
modeling. Includes a user-friendly interface to the packages 'pan' and 'jomo',
 and several functions for visualization, data management and the analysis 
 of multiply imputed data sets.

%prep
%setup -q -n mitml
cd %{_builddir}/mitml

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678470704

%install
export SOURCE_DATE_EPOCH=1678470704
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
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mitml/DESCRIPTION
/usr/lib64/R/library/mitml/INDEX
/usr/lib64/R/library/mitml/Meta/Rd.rds
/usr/lib64/R/library/mitml/Meta/data.rds
/usr/lib64/R/library/mitml/Meta/features.rds
/usr/lib64/R/library/mitml/Meta/hsearch.rds
/usr/lib64/R/library/mitml/Meta/links.rds
/usr/lib64/R/library/mitml/Meta/nsInfo.rds
/usr/lib64/R/library/mitml/Meta/package.rds
/usr/lib64/R/library/mitml/Meta/vignette.rds
/usr/lib64/R/library/mitml/NAMESPACE
/usr/lib64/R/library/mitml/NEWS
/usr/lib64/R/library/mitml/R/mitml
/usr/lib64/R/library/mitml/R/mitml.rdb
/usr/lib64/R/library/mitml/R/mitml.rdx
/usr/lib64/R/library/mitml/data/Rdata.rdb
/usr/lib64/R/library/mitml/data/Rdata.rds
/usr/lib64/R/library/mitml/data/Rdata.rdx
/usr/lib64/R/library/mitml/doc/Analysis.R
/usr/lib64/R/library/mitml/doc/Analysis.Rmd
/usr/lib64/R/library/mitml/doc/Analysis.html
/usr/lib64/R/library/mitml/doc/Introduction.R
/usr/lib64/R/library/mitml/doc/Introduction.Rmd
/usr/lib64/R/library/mitml/doc/Introduction.html
/usr/lib64/R/library/mitml/doc/Level2.R
/usr/lib64/R/library/mitml/doc/Level2.Rmd
/usr/lib64/R/library/mitml/doc/Level2.html
/usr/lib64/R/library/mitml/doc/index.html
/usr/lib64/R/library/mitml/help/AnIndex
/usr/lib64/R/library/mitml/help/aliases.rds
/usr/lib64/R/library/mitml/help/mitml.rdb
/usr/lib64/R/library/mitml/help/mitml.rdx
/usr/lib64/R/library/mitml/help/paths.rds
/usr/lib64/R/library/mitml/html/00Index.html
/usr/lib64/R/library/mitml/html/R.css
