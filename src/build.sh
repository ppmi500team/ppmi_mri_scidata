cdir=`pwd`
cd /Users/stnava/Documents/writing/ppmi_mri_scidata/src
Rscript -e 'rmarkdown::render("ppmi_sci_data.Rmd")'
cd $cdir
