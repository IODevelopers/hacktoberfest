class LocationHelper {

    /**
     * approximateTime
     * @param {Number} d // Must be in meters
     * @param {Number} s // Must be in m/s
     */
    approximateTime(d,s){
        var distance = +d;
        var speed = +s;
        var time = distance/speed;
        if(isNaN(time)) time = 0;
        return time;
    }

    /**
     * kmToMeters
     * @param {Number} d // Must be in km
     */
    kmToMeters(d){
        return +d * 1000;
    }

    /**
     * metersToKm
     * @param {Number} d // Must be in meters
     */
    metersToKm(d){
        return +d / 1000;
    }

    /**
     * degToRad
     * Converts numeric degrees to radians
     * @param {Number} i 
     */
    degToRad(i){
        return +i * Math.PI / 180;    
    }

    /**
     * distance
     * @param {Number} lat1 // From lat
     * @param {Number} lon1 // From Long
     * @param {Number} lat2 // To Lat
     * @param {Number} lon2 // From Lat
     */
    distance(lat1, lon1, lat2, lon2){
        var R = 6371;
        var dLat = this.degToRad(lat2-lat1);
        var dLon = this.degToRad(lon2-lon1);
        var lat1 = this.degToRad(lat1);
        var lat2 = this.degToRad(lat2);

        var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
        Math.sin(dLon/2) * Math.sin(dLon/2) * Math.cos(lat1) * Math.cos(lat2); 
        var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
        var d = R * c;
        return d;
    }

    /**
     * nearest
     * @param {Number} lat 
     * @param {Number} lon 
     * @param {Array} list // must contain 'latitude' and 'longitude' per elem
     */
    nearest(lat,lon,list){
        var mindif = 99999;
        var closest;
        for (var index = 0; index < list.length; ++index) {
			var dif = this.PythagorasEquirectangular(lat, lng, list[index].latitude, list[index].longitude);
			if (dif < mindif) {
			  closest = index;
			  mindif = dif;
			}
		}	
		return list[closest];
    }

    /**
     * PythagorasEquirectangular
     * @param {Number} lat1 
     * @param {Number} lon1 
     * @param {Number} lat2 
     * @param {Number} lon2 
     */
    PythagorasEquirectangular(lat1, lon1, lat2, lon2){
        lat1 = this.degToRad(lat1);
        lat2 = this.degToRad(lat2);
        lon1 = this.degToRad(lon1);
        lon2 = this.degToRad(lon2);
        var R = 6371; // Earth's radius in km
        var x = (lon2 - lon1) * Math.cos((lat1 + lat2) / 2);
        var y = (lat2 - lat1);
        var d = Math.sqrt(x * x + y * y) * R;
        return d;
    }

    /**
     * timeFormatter
     * @param {Number} secDouble //Seconds in double
     */
    timeFormatter(secDouble){
        var sec = +secDouble;
        var min = sec/60;
        var h = min/60;

        var time = {
            "hour":Math.trunc(h),
            "minutes":Math.trunc(min),
            "seconds":Math.trunc(sec)
        };

        return time;
    }
    
}