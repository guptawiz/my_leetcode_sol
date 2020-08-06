# def say_hello():
#     print 'Hello, World'
#
# for i in xrange(5):
#     say_hello()
# 
# Your previous Plain Text content is preserved below:
# 
# This is just a simple shared plaintext pad, with no execution capabilities.
# 
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
# 
# You can also change the default language your pads are created with
# in your account settings: https://coderpad.io/settings
# 
# Enjoy your interview!
# 
# ===== Preface =====
# 
# This question is very difficult in C and C++, where there is
# insufficient library support to answer it in an hour. If you
# prefer to program in one of those languages, please ask us to
# provide you with a question designed for those languages instead!
# 
# 
# ===== Intro =====
# 
# The Delphix San Francisco office is located in San Francisco’s
# financial district.  BART (Bay Area Rapid Transit) is a public
# transportation system serving the San Francisco Bay Area. Many
# engineers in the SF office use the Montgomery Street BART station
# to get to/from the office.
# 
# As engineers in the office will tell you, the BART system is
# infamously off schedule. Luckily, the BART public API
# (http://api.bart.gov/docs/overview/index.aspx) has a real-time
# information feed containing information about real-time estimated
# departures for specific stations. Your goal is to write a small
# program that utilizes the BART API that will quickly tell us the
# current time, the next 10 trains leaving Montgomery Street station,
# where they are going, and in how many minutes they leave the
# station.
# 
# Rules/constraints:
# * Print the trains in the order that they are leaving the station
# * Limit the output to the next 10 trains leaving the station
# * Print the number of minutes that the train will leave the station
# * Print the destination of the train
# 
# Example output:
# 
#     --------------------------------------------------
#     Montgomery St.  04:36:04 PM PDT
#     --------------------------------------------------
#     2 min  Dublin/Pleasanton
#     4 min  Daly City
#     5 min  Millbrae
#     5 min  Pittsburg/Bay Point
#     7 min  Fremont
#     9 min  Pleasant Hill
#     10 min  SF Airport
#     12 min  Daly City
#     12 min  Richmond
#     14 min  Millbrae
# 
# Your output does not need to match this, this is just an example.
# If you have better ideas of how to display the data, please do!
# 
# You should implement this in whatever language you're most
# comfortable with -- just make sure your code is production
# quality, well designed, and easy to read.
# 
# Finally, please help us by keeping this question and your
# answer secret so that every candidate has a fair chance in
# future Delphix interviews.
# 
# 
# ===== Steps =====
# 
# 1.  Choose the language you want to code in from the menu
#     labeled "Plain Text" in the top right corner of the
#     screen. You will see a "Run" button appear on the top
#     left -- clicking this will send your code to a Linux
#     server and compile / run it. Output will appear on the
#     right side of the screen.
#     
#     For information about what libraries are available for
#     your chosen language, see:
# 
#         https://coderpad.io/languages
# 
# 2.  Pull up the documentation for the API you'll be using:
# 
#       http://api.bart.gov/docs/etd/etd.aspx
# 
# 3.  You'll need an API key in order to query the data from
#     BART. You can create your own key
#     (http://www.bart.gov/schedules/developers/api) or use the demo
#     key:
# 
#         MW9S-E7SL-26DU-VV8V
# 
#     Make sure to use the API a bit to familiarize yourself 
#     with all of the outputs.
# 
# 4.  Implement the functionality described above, using data
#     fetched dynamically from the BART API described here:
# 
#       http://api.bart.gov/docs/etd/etd.aspx
# 
# 5.  Add any tests for your code to the main() method of
#     your program so that we can easily run them.
# 
# 
# 
# ====== FAQs =====
# 
# Q:  How do I know if my solution is correct?
# A:  Make sure you've read the prompt carefully and you're
#     convinced your program does what you think it should
#     in the common case. If your program does what the prompt 
#     dictates, you will get full credit. We do not use an
#     auto-grader, so we do not have any values for you to
#     check correctness against.
#     
# Q:  What is Delphix looking for in a solution?
# A:  After submitting your code, we'll have a pair of engineers
#     evaluate it and determine next steps in the interview process.
#     We are looking for correct, easy-to-read, robust code.
#     Specifically, ensure your code is idiomatic and laid out
#     logically. Ensure it is correct. Ensure it handles all edge
#     cases and error cases elegantly.
#     
# Q:  If I need a clarification, who should I ask?
# A:  Send all questions to the email address that sent you
#     this document, and an engineer at Delphix will get
#     back to you ASAP (we're pretty quick during normal
#     business hours).
# 
# Q:  How long should this question take me?
# A:  Approximately 1 hour, but it could take more or less
#     depending on your experience with web APIs and the
#     language you choose.
# 
# Q:  When is this due?
# A:  We will begin grading your answer 24 hours after it is
#     sent to you, so that is the deadline.
#     
# Q:  What if something comes up and I cannot complete the
#     problem during the 24 hours?
# A:  Reach out to us and let us know! We will work with you
#     to figure out an extension if necessary.
# 
# Q:  How do I turn in my solution?
# A:  Anything you've typed into this document will be saved.
#     Email us when you are done with your solution. We will
#     respond confirming we've received the solution within
#     24 hours.
# 
# Q:  Can I use any external resources to help me?
# A:  Absolutely! Feel free to use any online resources you
#     like, but please don't collaborate with anyone else.
# 
# Q:  Can I use my favorite library in my program?
# A:  Unfortunately, there is no way to load external
#     libraries into CoderPad, so you must stick to what
#     they provide out of the box for your language:
# 
#         https://coderpad.io/languages
# 
#     If you really want to use something that's not
#     available, email the address that sent you this link
#     and we will work with you to find a solution.
# 
# Q:  Can I code this up in a different IDE?
# A:  Of course! However, we do not have your environment
#     to run your code in. We ask that you submit your final
#     code via CoderPad (and make sure it can run). This gives
#     our graders the ability to run your code rather than guessing.
# 
# Q:  Why does my program terminate unexpectedly in
#     CoderPad, and why can't I read from stdin or pass
#     arguments on the command line?
# A:  CoderPad places a limit on the runtime and amount of
#     output your code can use, but you should be able to
#     make your code fit within those limits. You can hard
#     code any arguments or inputs to the program in your
#     main() method or in your tests.
# 
# Q:  I'm a Vim/Emacs fan -- is there any way to use those
#     keybindings? What about changing the tab width? Font
#     size?
# A:  Yes! Hit the button at the bottom of the screen that
#     looks like a keyboard.
#
#
#
# ====================================
# [code]
# ====================================
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re


class Bart:
    """
    ----- Bart API -----

    """
    # TEST CONSTANTS

    ETD_API_LINK = 'https://api.bart.gov/api/etd.aspx'
    STN_API_LINK = 'https://api.bart.gov/api/stn.aspx'
    MAX_LENGTH = 10

    def __init__(self, key='MW9S-E7SL-26DU-VV8V'):
        self.key = key

    def get_station_abbr(self, station_name):
        """
        Returns station abbreviation
        :param station_name: station name to match with station list
        """
        command = {'cmd': 'stns',
                   'key': self.key,
                   'json': 'y'
                   }
        result = requests.get(self.STN_API_LINK, params=command)
        if not result:
            return "No response for API : %s," % self.STN_API_LINK
        station_data = result.json()['root']['stations']
        for item in station_data.get('station'):
            st_name = item['name']
            if station_name == "ALL":
                raise Exception("No support for ALL stations")
            if re.search(station_name, st_name) or re.search(station_name, item['abbr']):
                return item['abbr']
        raise Exception("station : %s not found" % station_name)

    def etd(self, origin, platform=None, direction=None):
        """
        Returns estimated departure time for specified stations
        :param origin: specify station by their abbreviations
        :param platform: specific platform, ranges b/w 1-4,
        :param direction: direction, 'n' north; 's' south
        """

        estimate, station_info, info_dict, train_schedule = 'etd', '', {}, ''
        origin = self.get_station_abbr(origin)
        command = {'cmd': estimate,
                   'orig': origin,
                   'plat': platform,
                   'dir': direction,
                   'key': self.key,
                   'json': 'y'
                   }
        response = requests.get(self.ETD_API_LINK, params=command)
        if not response:
            return "No response for API : %s," % self.ETD_API_LINK
        data = response.json()['root']
        if "error" not in response.text:
            if not data.get('station') and data.get('message') != "":
                station_info += data['message']['warning']
                return station_info
            for station in data.get('station'):
                name = station['name']
                station_info += "\n\n%s\t%s\n\n" % (name, data['time'])
                if not station.get('etd'):
                    return "No scheduled trains from: %s" % name
                for location in station.get('etd'):
                    est = location.get('estimate')[0]
                    minutes = est['minutes']
                    destination = location['destination']
                    info_dict[minutes] = " " + "min" + "\t" + destination
        else:
            for station in data.get('station'):
                name = station['name']
                station_info += "\n\n%s\t%s\n\n" % (name, data['time'])
                if station.get('message'):
                    station_info += '%s' % station.get('message')['error']

        # handling a case where train is moving 'now' in order to sort
        if "Leaving" in info_dict.keys():
            info_dict[0] = info_dict.pop('Leaving')

        # * Trains in the order that they are leaving the station
        for key in sorted(info_dict.iterkeys(), key=int):
            # * Print the no. of minutes for trains leaving the station
            # * Print the destination of the train
            train_schedule += ("%s \t%s\n" % (key, info_dict[key]))

            # * Limit the output to the next 10 trains
            if len(train_schedule.split('\n')) > self.MAX_LENGTH:
                break
        return station_info + train_schedule


if __name__ == "__main__":
    bart = Bart()
    # print(bart.get_station_abbr(station_name="Mill"))
    print(bart.etd(origin="MONT"))


# ====================================
# [/code]
# ====================================
#
# ====================================
# [tests]
# ====================================
#
# case 1: stations are listed 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# Note : Used 'SBRN' as param to get all stations list)
# >>> 

# Prashant Gupta ran 379 lines of Python 2 (finished in 1.42s):

# San Bruno   09:47:00 PM PDT

# 7    min    SF Airport
# 41   min    SFO/Millbrae
# +++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#
#
# case 2 : Updates are temporarily unavailable
# ++++++++++++++++++++++++++++++++++++++++++++++++
# Note : o/p for 'MONT' station 
# >>>                                      (finished in 1.53s):
# Prashant Gupta ran 295 lines of Python 2:

# Montgomery St.  10:43:00 PM PDT

# Updates are temporarily unavailable.
# ++++++++++++++++++++++++++++++++++++++++++++++++
#
#
#
# case 3: valid station name is used instad of station abbr
# ++++++++++++++++++++++++++++++++++++++++++++++++
# Note : o/p for 'Pittsburg' station 
# >>> 
# Prashant Gupta ran 340 lines of Python 2 (finished in 1.41s):

# Pittsburg/Bay Point 10:43:00 PM PDT

# Updates are temporarily unavailable.
# ++++++++++++++++++++++++++++++++++++++++++++++++
#
#
# case 4: invalid station name (-ve scenario)
# ++++++++++++++++++++++++++++++++++++++++++++++++
# Note : o/p for 'ABCD' station 
# >>> 
# Prashant Gupta ran 351 lines of Python 2 (finished in 1.55s):

# Traceback (most recent call last):
#   File "/home/coderpad/solution.py", line 291, in <module>
#     print(bart.etd(origin="ABCD"))
#   File "/home/coderpad/solution.py", line 249, in etd
#     origin = self.get_station_abbr(origin)
#   File "/home/coderpad/solution.py", line 237, in get_station_abbr
#     raise Exception("station : %s not found" % station_name )
# Exception: station : ABCD not found.
# ++++++++++++++++++++++++++++++++++++++++++++++++
#
#
# Note : Additional code could be added to handle more cases 
# (additional + corner + invalid) as we increase the scope of testing. 
# for example : 
# 1.handling cases where multiple station names are same/similar
# 2.handling result for 'ALL' stations
# 3.handling uppercase/lowercase in different circumstances
