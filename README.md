# Counter Demographic Voting Trends

This project is still under construction; a rough model has been set up for Alabama's District 2-- this can be seen by clicking on Alabama on the app (jball-capstone.herokuapp.com).


## Purpose

The Counter Demographic Voting Trends project will be used to identify districts whose populations defy standard demographic voting trends. This information can be used by pollsters to target areas where populations are acting unusually in order to spot emerging trends faster. In addition, the demographic breakdown of the districts is information that could be useful in a number of ways and is the majority of the back-end work of this project.

The original idea was to use the demographic breakdown of districts in addition to speech analysis processing from election cycles and republican/democrat voter turnout reality vs. expectation to spot counter-party voting trends by identifying patterns between population demographics and election results.

When I began researching the datasets I would need for that project, I found that there was no data on these topics. While demographics are often used in voter prediction models, only the aggregate demographics are used and those are fed into machine learning models. Though this is a powerful tool, it is entirely useless for finding counterparty trends in specific demographic groups.

So this project detects outlier districts which will be instrumental for pollsters to find emerging trends, and lays a foundation which can be built up in future projects to provide guesses as to what those trends are.


## Bayesian Inference

The Problem: All demographic data is provided in aggregate (i.e. population is 55% female, 45% male; 10% didn't finish high school, 40% stopped at high school, 50% went to college; etc.). In order to locate counter-party demographic trends, it is necessary to determine the conjoined data (i.e. 0.2% white females age 35-45 who went to college and earn $70k-$90k a year). It is imperative to have the fully conjoined data to identify counter-party trends because a middle-aged white man with a high school diploma is statistically likely to have a different perspective than a middle-aged white man with a master's degree.

So the first and most challenging aspect of the project is to determine a way to mathmatically bin the populations by every relevant demographic category using only the national average statistics and the aggregate data for each population.

The Solution: I have worked out several states' voting estimation using a rough model in which several assumptions were made (i.e. that sex distribution was not dependent race and that age distribution was not dependent on race and sex). As these assumptions are incorrect, they can only give a very approximate guess.

My first thought was to use a Bayes Net and do something akin to a Monte Carlo throwing stones method modified to where the probabilities were altered in relation to the remaining sub-populations and the national average distributions. However, that would be a bit unwieldy, so for now, that is the backup option.

I am currently working on using a Bayesian Inference approach where the features are the aggregate data, the parameters are the conjoined demographic bins probable percentage of the total population, and the hyperparameter is the probability of my parameters being accurate. The initial guesses would be set equal to the national average likilihood of a given member of the population being in each bin, and new guesses would be determined using a Markov Chain Monte Carlo.
