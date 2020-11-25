# hasatellitetracker
Using the N2YO API, this Home Assistant integration provides visible satellite passes (general) and to add specific satellites for monitoring.

You will need to register for an API Key at <https://n2yo.com/api/>.

## Installation

To install this integration you will need to add <https://github.com/djtimca/hasatellitetracker> as a custom repository in HACS.

Once installed you will be able to install the integration from the HACS integrations page.

Restart your Home Assistant to complete the installation.

## Configuration

Go to Configuration -> Integrations and click the plus sign to add a Satellite Tracker integration. Search for Satellite Tracker (N2YO) and click add.

You will first need to enter your API key.

Second you will choose the type of integration you want to install:

### Location

A location integration will add a single sensor which will show you the number of satellites which are currently overhead, and in the attributes will list the satellites and their current positions.

If you select this option, on the next page you will enter:

- The name of the location you are tracking (default: the name of your Home Assistant instance)
- The category of satellites you want to track (default: all)
- The latitude of the location you want to track above (default: your Home Assistant latitude)
- The longitude of the location you want to track above (default: your Home Assistant longitude)
- The elevation of the location you want to track above (default: your Home Assistant elevation)

### Satellite

A satellite integration will add 5 sensors for the next visible passes and a device tracker sensor to allow you to plot the current location of a specific satellite on your map.

If you select this option, on the next page you will enter:

- The name of the satellite you want to track (default: International Space Station (ISS))
- The NORAD ID (from n2yo.com) you want to track (default: 25544 for the ISS)
- The latitude for visible pass tracking (default: Your Home Assistant latitude)
- The longitude for visible pass tracking (default: Your Home Assistant longitude)
- The elevation for visible pass tracking (default: Your Home Assistant elevation)

## Options

One you have set up an instance of the integration you also have additional options which can be configured by clicking "Options" on the integration.

### Location Integrations

- You can set the update interval in seconds for polling.
- You can specify the radius (degrees) for tracking satellites above (default 90).

### Satellite Integrations

- You can set the update interval in seconds for polling.
- You can specify the minimum number of seconds you want to have for a visible pass.

# Important Note

The N2YO API is rate limited to 1000 transactions per hour. Adding a large number of integrations or setting your polling / update interval too low may result in your API key from being suspended or banned.

