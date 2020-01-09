from email_reply_parser import EmailReplyParser

message = """Jacques,

Here is Larry Lewter's response to my request for more documentation to 
support the $15,000.  As you will read below, it is no longer an issue.  I 
think that was the last issue to resolve. 

Phillip


---------------------- Forwarded by Phillip K Allen/HOU/ECT on 03/19/2001 
11:45 AM ---------------------------


"Larry Lewter" <llewter@austin.rr.com> on 03/19/2001 09:10:33 AM
To: <Phillip.K.Allen@enron.com>
cc:  
Subject: RE: Buyout


Phillip, the title company held the $15,000 in escrow and it has been
returned. It is no longer and issue.
Larry

-----Original Message-----
From: Phillip.K.Allen@enron.com [mailto:Phillip.K.Allen@enron.com]
Sent: Monday, March 19, 2001 8:45 AM
To: llewter@austin.rr.com
Subject: Re: Buyout



Larrry,

I realize you are disappointed about the project.  It is not my desire for
you to be left with out of pocket expenses.  The only item from your list
that I need further
clarification is the $15,000 worth of extensions.  You mentioned that this
was applied to the cost of the land and it actually represents your cash
investment in the land.  I agree that you should be refunded any cash
investment.  My only request is that you help me locate this amount on the
closing statement or on some other document.

Phillip

"""
message1 ="""
:+1:

On Tue, Sep 25, 2012 at 8:59 AM, Chris Wanstrath
<notifications@github.com>wrote:

> Steps 0-2 are in prod. Gonna let them sit for a bit then start cleaning up
> the old code with 3 & 4.
>
> 
> Reply to this email directly or view it on GitHub.
>
>"""

# EmailReplyParser.read(message1)
print(EmailReplyParser.parse_reply(message1))

# print(body)