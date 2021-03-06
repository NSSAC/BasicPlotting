#Specify values here

input_file="houston.rank.out"
output_file="houston.rank.out"
xCol="1"
yCol="0"
delimter=","
title="Houston_Page_Rank"
xLabel="Page_Rank_Scores"
yLabel="Fraction_of_Nodes"

baseinDir="test/test_data"
baseoutDir="test/test_results"

python ./src/BinPlotGen.py \
	./${baseinDir}/${input_file} \
	./${baseoutDir}/${output_file} \
	$xCol \
	$yCol \
	$delimter \
	$title \
	$xLabel \
	$yLabel
