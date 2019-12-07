odoo.define('web_calendar_extensions.web_calendar_extensions', function (require) {
    "use strict";

    var CalendarView = require('web_calendar.CalendarView');

    // TODO These options shall be changed by Odoo (user)settings or parameters
    CalendarView.include({
        get_fc_init_options: function () {
            var options = this._super.apply(this, arguments);
            options.slotMinutes = 5;
            options.snapMinutes = 5;
            options.firstHour = (new Date().getHours() - 1);
            options.minTime = 6;
            options.maxTime = 18;
            
            return options;
        }
    });
});
