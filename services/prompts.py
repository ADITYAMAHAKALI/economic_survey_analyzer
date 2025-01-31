SUMMARIZER_PROMPT = """
Summarize the following document in an engaging and insightful manner:

Title: {title}
Content: {content}

Provide the summary in the following structured format:
<JSON>
{{
  "Philosophy_of_Policy_Makers": "Describe the core philosophy, vision, and strategic intent behind the policies.",
  "Previous_Performance_Summary": "Highlight key achievements, challenges, and sector-wise performance in the previous period.",
  "Future_Predictions": "Summarize economic forecasts, projected trends, and policy implications.",
  "Focus_Areas_and_Sectors": "List priority sectors, key investment areas, and companies likely to benefit.",
  "Key_Policy_Changes_and_Reforms": "Outline significant policy shifts, regulatory updates, and governance changes.",
  "Growth_Drivers_and_Challenges": "Identify factors fueling economic growth and potential hurdles to watch for.",
  "Global_Impact_and_Comparisons": "Provide insights on how India's economic trends align with global markets and peer economies.",
  "Opportunities_for_Businesses_and_Investors": "Highlight lucrative opportunities, potential high-growth areas, and investment insights.",
  "Technology_and_Innovation_Impact": "Describe the role of AI, digital transformation, and emerging tech in shaping economic policies.",
  "Social_Implications": "Examine how the policies affect employment, education, healthcare, and social welfare.",
  "Conclusion_and_Actionable_Insights": "Summarize key takeaways, strategic recommendations, and next steps for stakeholders."
}}
</JSON>
"""
temp="""
Pydantic Schema: {{'properties': {{'Philosophy_of_Policy_Makers': {{'description': 'Core philosophy and strategic intent of policymakers.',
   'title': 'Philosophy Of Policy Makers',
   'type': 'string'}},
  'Previous_Performance_Summary': {{'description': 'Key achievements and challenges in the previous period.',
   'title': 'Previous Performance Summary',
   'type': 'string'}},
  'Future_Predictions': {{'description': 'Economic forecasts and expected trends.',
   'title': 'Future Predictions',
   'type': 'string'}},
  'Focus_Areas_and_Sectors': {{'description': 'Sectors of interest and companies to watch.',
   'title': 'Focus Areas And Sectors',
   'type': 'string'}},
  'Key_Policy_Changes_and_Reforms': {{'description': 'Significant policy updates and regulatory changes.',
   'title': 'Key Policy Changes And Reforms',
   'type': 'string'}},
  'Growth_Drivers_and_Challenges': {{'description': 'Factors driving growth and potential challenges.',
   'title': 'Growth Drivers And Challenges',
   'type': 'string'}},
  'Global_Impact_and_Comparisons': {{'description': "Comparison of India's economy with global trends.",
   'title': 'Global Impact And Comparisons',
   'type': 'string'}},
  'Opportunities_for_Businesses_and_Investors': {{'description': 'High-growth areas and investment opportunities.',
   'title': 'Opportunities For Businesses And Investors',
   'type': 'string'}},
  'Technology_and_Innovation_Impact': {{'description': 'Role of AI, digital transformation, and emerging technologies.',
   'title': 'Technology And Innovation Impact',
   'type': 'string'}},
  'Social_Implications': {{'description': 'Effects on employment, education, and social welfare.',
   'title': 'Social Implications',
   'type': 'string'}},
  'Conclusion_and_Actionable_Insights': {{'description': 'Key takeaways and recommendations.',
   'title': 'Conclusion And Actionable Insights',
   'type': 'string'}}}},
 'required': ['Philosophy_of_Policy_Makers',
  'Previous_Performance_Summary',
  'Future_Predictions',
  'Focus_Areas_and_Sectors',
  'Key_Policy_Changes_and_Reforms',
  'Growth_Drivers_and_Challenges',
  'Global_Impact_and_Comparisons',
  'Opportunities_for_Businesses_and_Investors',
  'Technology_and_Innovation_Impact',
  'Social_Implications',
  'Conclusion_and_Actionable_Insights'],
 'title': 'SummaryStructure',
 'type': 'object'}}
 """