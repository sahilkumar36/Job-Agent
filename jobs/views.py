from django.shortcuts import render, redirect
from .models import Job
from .agent import analyze_job, extract_text_from_pdf

def home(request):
    """
    Main dashboard showing analyzed jobs.
    """
    jobs = Job.objects.all().order_by('-date_posted')
    return render(request, 'jobs/home.html', {'jobs': jobs})

def analyze_job_view(request):
    """
    View to handle job description submission and AI analysis.
    """
    if request.method == 'POST':
        description = request.POST.get('description')
        user_skills = request.POST.get('user_skills', '')
        resume_file = request.FILES.get('resume')
        
        # If a resume is uploaded, extract text from it
        if resume_file:
            try:
                extracted_skills = extract_text_from_pdf(resume_file)
                user_skills = f"{user_skills}\n\nExtracted from Resume:\n{extracted_skills}"
            except Exception as e:
                return render(request, 'jobs/analyze.html', {'error': f"Failed to parse PDF: {str(e)}"})
        
        # Analyze using the AI agent
        try:
            analysis = analyze_job(description, user_skills)
            
            # Create a job entry with AI analysis
            job = Job.objects.create(
                title=request.POST.get('title', 'Analyzed Job'),
                company=request.POST.get('company', 'Unknown Company'),
                description=description,
                url=request.POST.get('url', 'http://example.com'),
                ai_summary=analysis.get('summary', ''),
                match_score=analysis.get('match_score', 0),
                skills_found=analysis.get('skills_found', []),
                missing_skills=analysis.get('missing_skills', []),
                ai_advice=analysis.get('advice', '')
            )
            return redirect('home')
        except Exception as e:
            # Handle API errors or parsing issues
            return render(request, 'jobs/analyze.html', {'error': str(e)})
            
    return render(request, 'jobs/analyze.html')
