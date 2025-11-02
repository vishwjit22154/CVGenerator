import { useState } from 'react';
import { useForm } from 'react-hook-form';
import toast from 'react-hot-toast';
import { Loader2, Send } from 'lucide-react';
import { coverLetterAPI } from '../services/api';

function CoverLetterForm({ onGenerate }) {
  const [isGenerating, setIsGenerating] = useState(false);
  const { register, handleSubmit, formState: { errors } } = useForm({
    defaultValues: {
      resume_text: '',
      job_description: '',
      ai_provider: 'claude',
      template_style: 'professional',
      tone: 'formal',
      word_count: 300,
    }
  });

  const onSubmit = async (data) => {
    setIsGenerating(true);
    
    const loadingToast = toast.loading('Generating your cover letter...');
    
    try {
      const result = await coverLetterAPI.generateCoverLetter(data);
      
      toast.success(`Generated in ${result.generation_time}s!`, {
        id: loadingToast,
      });
      
      onGenerate(result, data);
    } catch (error) {
      console.error('Error generating cover letter:', error);
      toast.error(
        error.response?.data?.detail || 'Failed to generate cover letter. Please try again.',
        { id: loadingToast }
      );
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className="card max-w-4xl mx-auto">
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
        {/* Main Inputs - Only 2 Required! */}
        <div className="space-y-4">

          <div>
            <label className="label">
              Resume *
            </label>
            <textarea
              {...register('resume_text', { required: 'Resume is required' })}
              className="input-field font-mono text-sm"
              rows="10"
              placeholder="Paste your complete resume here...

John Doe
john@email.com | (555) 123-4567
linkedin.com/in/johndoe

EXPERIENCE
Senior Software Engineer | Tech Company | 2020-Present
- Led development of...
- Implemented...

EDUCATION
Bachelor of Science in Computer Science | University Name | 2018

SKILLS
Python, JavaScript, React, Node.js, AWS..."
            />
            {errors.resume_text && (
              <p className="text-red-500 text-sm mt-1">{errors.resume_text.message}</p>
            )}
          </div>
          
          <div>
            <label className="label">
              Job Posting *
            </label>
            <textarea
              {...register('job_description', { required: 'Job description is required' })}
              className="input-field font-mono text-sm"
              rows="12"
              placeholder="Paste the complete job posting here...

Senior Full Stack Developer
TechCorp Inc. | San Francisco, CA

About the Company:
TechCorp is a leading technology company...

Job Description:
We are seeking a talented Full Stack Developer with 5+ years of experience in React, Node.js...

Requirements:
- 5+ years of professional experience
- Strong proficiency in JavaScript, React, Node.js
- Experience with cloud platforms (AWS/GCP)
..."
            />
            {errors.job_description && (
              <p className="text-red-500 text-sm mt-1">{errors.job_description.message}</p>
            )}
          </div>

          <div>
            <label className="label">Additional Notes (Optional)</label>
            <textarea
              {...register('additional_notes')}
              className="input-field"
              rows="2"
              placeholder="Any specific requirements or things to emphasize? (optional)"
            />
          </div>
        </div>

        {/* Customization Section */}
        <div className="space-y-4">
          <h3 className="text-lg font-semibold text-gray-900 border-b pb-2">
            Options
          </h3>
          
          <div className="grid md:grid-cols-2 gap-4">
            <div>
              <label className="label">AI Provider</label>
              <select {...register('ai_provider')} className="input-field">
                <option value="claude">Claude (Anthropic)</option>
                <option value="openai">ChatGPT (OpenAI)</option>
              </select>
            </div>
            
            <div>
              <label className="label">Template Style</label>
              <select {...register('template_style')} className="input-field">
                <option value="professional">Professional</option>
                <option value="creative">Creative</option>
                <option value="technical">Technical</option>
                <option value="executive">Executive</option>
              </select>
            </div>
            
            <div>
              <label className="label">Tone</label>
              <select {...register('tone')} className="input-field">
                <option value="formal">Formal</option>
                <option value="conversational">Conversational</option>
                <option value="enthusiastic">Enthusiastic</option>
                <option value="confident">Confident</option>
              </select>
            </div>
            
            <div>
              <label className="label">Target Word Count</label>
              <input
                {...register('word_count', { 
                  min: 100, 
                  max: 800,
                  valueAsNumber: true 
                })}
                type="number"
                className="input-field"
                min="100"
                max="800"
              />
            </div>
          </div>
        </div>

        {/* Submit Button */}
        <div className="flex justify-center pt-4">
          <button
            type="submit"
            disabled={isGenerating}
            className="btn-primary flex items-center space-x-2 px-8 py-4 text-lg"
          >
            {isGenerating ? (
              <>
                <Loader2 className="w-5 h-5 animate-spin" />
                <span>Generating...</span>
              </>
            ) : (
              <>
                <Send className="w-5 h-5" />
                <span>Generate Cover Letter</span>
              </>
            )}
          </button>
        </div>
      </form>
    </div>
  );
}

export default CoverLetterForm;

