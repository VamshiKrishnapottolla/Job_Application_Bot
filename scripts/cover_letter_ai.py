from openai import OpenAI

client = OpenAI()

def generate_cover_letter(job_title, company_name, resume_summary):
    prompt = f"""
    Write a short, professional cover letter for a {job_title} position at {company_name}.
    Base it on this résumé summary: {resume_summary}.
    Make it ATS-friendly and under 150 words.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
