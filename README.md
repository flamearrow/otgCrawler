# otgCrawler
crawl off the grid website for their weekly schedules
Usage: python otg_request.py
The script will go though OTGMarketsJson.json(which is hard coded at the moment) for each of its id and use 'http://offthegridsf.com/wp-admin/admin-ajax.php?action=otg_market&delta=0&market=' to pull all schedules of THIS week.
Result is written to out.json as a list of following event objects:

{
        "end":"0900",
        "latitude":"37.415237",
        "longitude":"-122.077637",
        "start":"1700",
        "address":"1401 North Shoreline Boulevard , Mountain View",
        "date":"0515",
        "truck_name":"Gold Rush Eatery"
}

We may do something smart to hook this up with the schedule inputer...
