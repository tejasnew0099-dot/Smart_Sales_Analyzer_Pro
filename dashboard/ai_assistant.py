"""
ai_assistant.py
------------------------------------
AI Assistant (Rule-Based Version)
"""


def answer_question(question, df, kpis):
    """
    Answer common business questions
    """

    if question == "Which region generated the highest sales?":

        region = (
            df.groupby("Region")["Net Sales"]
            .sum()
            .idxmax()
        )

        sales = (
            df.groupby("Region")["Net Sales"]
            .sum()
            .max()
        )

        return (
            f"🏆 {region} generated the highest sales "
            f"with ₹{sales:,.2f}."
        )

    elif question == "Who is the top customer?":

        customer = (
            df.groupby("Customer Name")["Net Sales"]
            .sum()
            .idxmax()
        )

        sales = (
            df.groupby("Customer Name")["Net Sales"]
            .sum()
            .max()
        )

        return (
            f"👤 {customer} is the top customer "
            f"with purchases of ₹{sales:,.2f}."
        )

    elif question == "Which brand performs the best?":

        return (
            f"🥇 {kpis['Best Brand']} "
            "is currently the best-performing brand."
        )

    elif question == "Which region performs the best?":

        return (
            f"🌍 {kpis['Best Region']} "
            "is the best-performing region."
        )

    else:

        return (
            "🤖 AI Assistant is ready. "
            "More intelligent answers are coming soon!"
        )