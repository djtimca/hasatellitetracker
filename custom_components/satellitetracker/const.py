"""Constants for the Satellite Tracker integration."""

DOMAIN = "satellitetracker"
COORDINATOR = "coordinator"
SATELLITE_API = "n2yo_api"
ATTR_IDENTIFIERS = "identifiers"
ATTR_MANUFACTURER = "manufacturer"
ATTR_MODEL = "model"
CONF_MIN_VISIBILITY = "min_visibility"
CONF_SATELLITE = "satellite"
DEFAULT_POLLING_INTERVAL = 10
DEFAULT_MIN_VISIBILITY = 300
TRACKER_TYPE = {
    "0": "location",
    "1": "satellite",
}
