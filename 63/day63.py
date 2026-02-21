# Building an AI Resume Screener 📄 (Day 63)
# pip install scikit-learn

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Job Description ---
job_description = """
We are looking for a Python Developer with experience in Machine Learning, 
Data Science, and web development using Django or Flask. 
The ideal candidate should have knowledge of SQL databases, REST APIs, 
Git version control, and cloud deployment (AWS or GCP).
Strong problem-solving skills and teamwork are essential.
"""

# --- Candidate Resumes ---
resumes = {
    "Aarav Sharma": """
        Python developer with 3 years of experience in Machine Learning and Data Science.
        Built REST APIs using Flask and Django. Proficient in SQL, PostgreSQL, and MongoDB.
        Deployed ML models on AWS EC2 and S3. Strong Git workflow. Team player.
    """,
    "Priya Patel": """
        Frontend developer skilled in React, JavaScript, HTML, CSS, and Tailwind.
        Experience with Firebase and Node.js backend. Good understanding of UI/UX design.
        Familiar with Git and Agile methodology. Built several e-commerce websites.
    """,
    "Rohan Gupta": """
        Full-stack developer with Python, Django, and React experience.
        Knowledge of Machine Learning basics using scikit-learn and pandas.
        Worked with REST APIs, SQL databases, and Docker. Deployed apps on GCP.
        Open source contributor with strong problem-solving skills.
    """,
    "Sneha Reddy": """
        Data Scientist with expertise in Python, TensorFlow, and Keras.
        Experience in NLP, Computer Vision, and deep learning model deployment.
        Proficient in pandas, numpy, matplotlib, and SQL.
        Published research papers in ML. AWS certified cloud practitioner.
    """,
    "Karan Mehta": """
        Java developer with Spring Boot and microservices architecture experience.
        Knowledge of Oracle SQL, REST APIs, and CI/CD pipelines.
        Familiar with Docker, Kubernetes, and Azure cloud. Certified Scrum Master.
    """
}

print("=" * 60)
print("🤖 AI Resume Screener | Day 63")
print("=" * 60)

# --- Display Job Description ---
print("\n📋 JOB DESCRIPTION:")
print("-" * 40)
print(job_description.strip())
print("-" * 40)

# --- TF-IDF + Cosine Similarity ---
# Combine job description with all resumes for vectorization
documents = [job_description] + list(resumes.values())

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

# Compare each resume against job description (index 0)
scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

# --- Results ---
print("\n📊 CANDIDATE RANKING:")
print("=" * 60)
print(f"{'Rank':<6} {'Candidate':<20} {'Match %':<12} {'Status'}")
print("-" * 60)

# Pair names with scores and sort
results = list(zip(resumes.keys(), scores))
results.sort(key=lambda x: x[1], reverse=True)

for rank, (name, score) in enumerate(results, 1):
    percentage = score * 100

    # Status based on match percentage
    if percentage >= 40:
        status = "✅ SHORTLISTED"
    elif percentage >= 25:
        status = "🟡 MAYBE"
    else:
        status = "❌ REJECTED"

    print(f"#{rank:<5} {name:<20} {percentage:>6.1f}%      {status}")

print("=" * 60)

# --- Top Candidate Summary ---
top_name, top_score = results[0]
print(f"\n🏆 TOP CANDIDATE: {top_name} ({top_score * 100:.1f}% match)")
print(f"\n💡 TIP: This screener uses TF-IDF vectorization to convert")
print(f"   text into numbers and cosine similarity to find the best match.")
print(f"   It's the same tech used by real ATS (Applicant Tracking Systems)!")