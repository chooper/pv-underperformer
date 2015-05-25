# pv-underperformers

A Python script to identify underperforming PV (solar) systems in
performance data reported by
[californiasolarstatistics.ca.gov](https://www.californiasolarstatistics.ca.gov/current_data_files/).

Currently, this script defines *underperformance* as installations whose
mean output from all reported periods is less than its zip code's mean
by at least one standard deviation.

Future versions will account for installation cost.

## Usage

```bash
$ docker-compose build
$ docker-compose run app
```

If you don't use Docker, the following will work:

```bash
$ python3 ./app.py
```

## Current underperformers

```
Underperformer! id=SD-CSI-00618 output=600.7666666666667kWh zip-mean=845.8513931888544kWh zip-stdev=237.89781651976162
Underperformer! id=SD-CSI-07219 output=345.2352941176471kWh zip-mean=857.046783625731kWh zip-stdev=423.22784723691024
Underperformer! id=SCE-CSI-22852 output=645.4411764705883kWh zip-mean=1383.790333560245kWh zip-stdev=630.0574532798172
Underperformer! id=SCE-CSI-20332 output=610.3023255813954kWh zip-mean=1383.790333560245kWh zip-stdev=630.0574532798172
Underperformer! id=SD-CSI-00612 output=297.21666666666664kWh zip-mean=576.4666666666667kWh zip-stdev=235.62912006418526
Underperformer! id=SCE-CSI-05440 output=660.0833333333334kWh zip-mean=1181.0801131008482kWh zip-stdev=464.26884557457277
Underperformer! id=SCE-CSI-08184 output=692.0833333333334kWh zip-mean=1181.0801131008482kWh zip-stdev=464.26884557457277
Underperformer! id=SCE-CSI-07537 output=526.3559322033898kWh zip-mean=1105.628346456693kWh zip-stdev=455.564622052426
Underperformer! id=SD-CSI-09769 output=703.475kWh zip-mean=1361.53kWh zip-stdev=603.206058573685
Underperformer! id=SD-CSI-04923 output=842.4666666666667kWh zip-mean=1415.8041237113403kWh zip-stdev=551.3867236530053
```

