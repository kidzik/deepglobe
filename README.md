# Satellite image analysis

## Usage

1. Put `.png` your images in `input/`
2. Run
```
python2 main.py [model_name]
```
where `[model_name]` is one of: `building-non-residential`, `building`, `cars`, `fields`, `roads`, `trees`, or `unpaved_roads`
3. Find results in `output/[model_name]`

## Downloading an image

I use zoom 17 and the following code:
```
wget 'http://maps.googleapis.com/maps/api/staticmap?center=Marszalkowska%206a,%2005-840%20Warszawa&zoom=17&maptype=satellite&size=1000x1000&key=[GOOGLE_MAPS_API_KEY]' -O input/1.png
```