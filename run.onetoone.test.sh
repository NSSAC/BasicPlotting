#Specify values here

input_file="houston.deg.distro.out"
output_file="houston.deg.distro"
xCol="0"
yCol="1"
title="Houston_Degree_Distribution"
xLabel="Degree"
yLabel="Number_of_Nodes"

baseinDir="test/test_data"
baseoutDir="test/test_results"



python ./src/OneToOnePlotGen.py \
	./${baseinDir}/${input_file} \
	./${baseoutDir}/${output_file} \
	$xCol \
	$yCol \
	$title \
	$xLabel \
	$yLabel
