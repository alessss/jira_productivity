__author__ = 'a_makarevich'

import requests, json, datetime
from datetime import timedelta, date

#jql = "http://jira.wargaming.net/rest/api/2/search/?jql=status+changed+to+Closed+during+(-12d,+-5d)+AND+status+changed+by+(a_makarevich,+a_sidyakin,+a_dorogokupets,+d_pluzhnikov,+n_novogran)+and+issuetype="
#us_jql = "http://jira.wargaming.net/rest/api/2/search/?jql=status+changed+to+Closed+during+(-12d,+-5d)+AND+status+changed+by+(a_makarevich,+a_sidyakin,+a_dorogokupets,+d_pluzhnikov,+n_novogran)"






def date_minuser(n):
    day = -1
    while day > n:
        jql2 = "http://jira.wargaming.net/rest/api/2/search/?jql=status+changed+to+Closed+during+("+str(day)+"d,+"+str(day+1)+"d)+AND+status+changed+by+(a_makarevich,+a_sidyakin,+a_dorogokupets,+d_pluzhnikov,+n_novogran,+d_khotenko)+and+issuetype="
        us_jql2 = "http://jira.wargaming.net/rest/api/2/search/?jql=status+changed+to+Closed+during+("+str(day)+"d,+"+str(day+1)+"d)+AND+status+changed+by+(a_makarevich,+a_sidyakin,+a_dorogokupets,+d_pluzhnikov,+n_novogran,d_khotenko)"
#        jql2 = "http://jira.wargaming.net/rest/api/2/search/?jql=status+changed+to+Closed+during+("+str(day)+"d,+"+str(day+1)+"d)+AND+status+changed+by+(d_khotenko)+and+issuetype="
#        us_jql2 = "http://jira.wargaming.net/rest/api/2/search/?jql=status+changed+to+Closed+during+("+str(day)+"d,+"+str(day+1)+"d)+AND+status+changed+by+(d_khotenko)"


        date_tod = date.today()
        yest_date = date_tod - datetime.timedelta(days=abs(day))
        print ' '
        print 'on day'+' '+str(yest_date)+' '+'done'
        issues_closed(all_issues_closed=us_closed(us_jql2),jql2=jql2)
        day = day-1


def us_closed(us_jql2):
    a = requests.get(us_jql2, auth=('a_makarevich', 'C345jklmno98765432'))
    b = json.loads(a.text)
    all_issues_closed = b['total']
    print 'total issues closed' + ' ' + str(all_issues_closed)
    return all_issues_closed


def issues_closed(all_issues_closed,jql2):
    issuetype = ['bug', 'task', 'improvement']
    for i in issuetype:
        a = requests.get(jql2 + i, auth=('a_makarevich', 'C345jklmno98765432'))
        b = json.loads(a.text)
        all_issues_closed = all_issues_closed - b['total']
        print i + ' ' + 'closed' + ' ' + str(b['total'])
    print 'User Stories closed' + ' ' + str(all_issues_closed)


print date_minuser(-50)