import { Zap, Copy, Brain, Download } from 'lucide-react';

const features = [
  {
    icon: Copy,
    title: 'Super Simple',
    description: 'Just copy-paste your resume and job posting - that\'s it!',
  },
  {
    icon: Brain,
    title: 'Smart AI Analysis',
    description: 'AI extracts company, role, and matches your experience automatically',
  },
  {
    icon: Zap,
    title: 'Instant Generation',
    description: 'Professional cover letter ready in 10-15 seconds',
  },
  {
    icon: Download,
    title: 'Multiple Formats',
    description: 'Download as PDF, DOCX, or TXT instantly',
  },
];

function Features() {
  return (
    <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      {features.map((feature, index) => (
        <div
          key={index}
          className="bg-white rounded-lg p-6 shadow-md hover:shadow-xl transition-shadow duration-300"
        >
          <div className="bg-primary-100 w-12 h-12 rounded-lg flex items-center justify-center mb-4">
            <feature.icon className="w-6 h-6 text-primary-600" />
          </div>
          <h3 className="text-lg font-semibold text-gray-900 mb-2">
            {feature.title}
          </h3>
          <p className="text-gray-600 text-sm">{feature.description}</p>
        </div>
      ))}
    </div>
  );
}

export default Features;

