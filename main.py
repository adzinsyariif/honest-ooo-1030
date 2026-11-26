"""Painfully honest out-of-office auto-reply (one sentence, <=200 chars).

Judge criteria (competition.yaml), most important first:
  1. Painfully honest AND still polite (both, or it loses).
  2. Admits a private truth about absence / workload / inbox.
  3. Warm, professional tone a manager would let stand.
  4. One sentence, <=200 chars, no cramming or trailing off.
  5. A quotable turn of phrase, not a list of complaints.

Four candidates of my own, scored 1-5 per criterion (H=honesty,
P=politeness/manager-safe, Q=quotable phrase; all are one sentence
within the limit, so criterion 4 passes for each):

  C1 "I am out of office and will read your email on my return with
      the enthusiasm of someone whose inbox is already a small,
      polite cry for help, but I will reply - thank you for your
      patience."
      H4 P5 Q4 -- honest about enthusiasm, very safe, a bit long.

  C2 "I am on leave until Monday and have bravely decided not to
      check email, so this message will be lovingly ignored until
      then - thank you for understanding."
      H4 P4 Q3 -- admits ignoring mail; 'lovingly ignored' risks
      reading as rude when forwarded.

  C3 "I am away from my desk and, in the interest of honesty, away
      from any desire to open my inbox until I return, when I will
      greet your email as if we have never met - thank you for your patience."
      H5 P4 Q4 -- the most private truth (no desire at all); the
      'never met' turn is funny but slightly cold.

  C4 "I am out of office and will respond on my return; if it is
      urgent, please consider this reply proof that even my
      auto-reply is trying its best to help."
      H2 P5 Q3 -- polite and cute, but admits nothing real.

Follow-up round (later session): three fresh alternatives of my
own, scored the same way, to test whether C3 still wins:

  C5 "I am out of office and your email has joined several hundred
      others I will greet with sincere apologies and fresh coffee
      when I return - thank you for your patience."
      H4 P5 Q4 -- honest about the pileup, warmest of the set;
      but the truth is about volume, not reluctance, so it is
      less painfully honest than C3 on criterion 2.

  C6 "I am on leave and, to be honest, not thinking about work at
      all, but I will give your email my full attention when I
      return - thank you for your patience."
      H5 P3 Q2 -- the barest admission, but 'not thinking about
      work at all' is the riskiest line to forward to a manager
      (criterion 3) and the phrasing is flat (criterion 5).

  C7 "I am out of office and happily not checking email, which I
      will face with great bravery on my return - thank you for
      understanding."
      H4 P4 Q3 -- 'happily not checking' is honest, but 'great
      bravery' is generic and less quotable than the old-friend
      turn.

Verdict of the follow-up round: none beats C3's frame. C5 is
warmer but less honest; C6 is honester but less manager-safe and
less quotable; C7 is thinner on both. The right move is to
sharpen C3's wording, not replace its concept.

Winner: C3 (highest honesty, the judge's first criterion, while
staying professional). Two revisions then tighten it:

  Revision 1: give it a warm, manager-proof closing ('thank you for
  your patience') so the honesty cannot be read as hostility.
  Revision 2: sharpen the quotable turn -- greeting the email 'like
  an old friend I have been avoiding' is warmer and funnier than
  'as if we have never met', and trims the sentence.

  Revision 3 (follow-up): fix the opening parallelism. 'away from
  any desire to open' was abstract and sounded lazy; 'in no hurry
  to open my inbox' is the same private truth in understatement,
  more natural and more manager-safe. 'but when I return I will
  greet...' folds the promise of action into the sentence instead
  of bolting it on with a dash, so it reads as one breath.

  Revision 4 (final tightening): 'when I return' -> 'on my return'
  (the idiomatic OOO phrasing, one breath shorter) and 'I have
  been avoiding' -> "I've been avoiding" (a contraction sounds
  like a real person, warmer and more quotable, and the smaller
  text helps the Size tie-break). Honesty and the manager-safe
  closing are untouched.
"""

import os

ENTRY = (
    "I am out of office and, honestly, in no hurry to open my "
    "inbox, but on my return I will greet your email like an old "
    "friend I've been avoiding — thank you for your patience."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
