#!/usr/bin/env python3
"""Structural scan of all Active Inference course modules."""

import sys
import json
import logging
from pathlib import Path

# Add software directory to path
software_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(software_dir))

from src.batch_processing.config import COURSE_REGISTRY
from src.content_processing.structure_scan import scan_course, format_report

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    repo_root = software_dir.parent
    
    logger.info("Starting structural scan of modules...")
    
    all_issues = []
    stats = {
        "total_modules_expected": 0,
        "total_modules_found": 0,
        "total_files_checked": 0,
        "missing_files": 0,
        "small_files": 0,
        "placeholders": 0,
        "quiz_issues": 0,
        "question_count_issues": 0,
        "learning_obj_issues": 0,
        "broken_links": 0,
        "missing_module_dirs": 0,
    }
    course_summaries = {}

    # Sort courses by ID for consistent output
    for course_id, config in sorted(COURSE_REGISTRY.items()):
        # Skip Youtube transcripts as they have different structure/requirements
        if course_id == "youtube":
            continue
            
        logger.info(f"Scanning {course_id}...")
        
        course_stats, summary, issues = scan_course(course_id, config, repo_root)
        
        # Merge stats
        for k, v in course_stats.items():
            if k in stats:
                stats[k] += v
                
        course_summaries.update(summary)
        all_issues.extend(issues)

    # Format report
    report = format_report(stats, course_summaries, all_issues, str(repo_root))
    print(report)

    # Save to file (using original location for continuity)
    report_path = repo_root / "structural_scan_report.txt"
    report_path.write_text(report, encoding="utf-8")
    logger.info(f"\nReport saved to: {report_path}")

    # Save raw data as JSON
    json_path = repo_root / "structural_scan_data.json"
    json_data = {
        "stats": stats,
        "course_summaries": {k: {
            **v,
            # Ensure sets/lists are serializable if any remain (though structure_scan uses lists)
        } for k, v in course_summaries.items()},
        "issues_count": len(all_issues),
        "issues_by_type": {}
    }
    
    for iss in all_issues:
        t = iss["type"]
        if t not in json_data["issues_by_type"]:
            json_data["issues_by_type"][t] = []
        json_data["issues_by_type"][t].append(iss)

    json_path.write_text(json.dumps(json_data, indent=2), encoding="utf-8")
    logger.info(f"JSON data saved to: {json_path}")

if __name__ == "__main__":
    main()
