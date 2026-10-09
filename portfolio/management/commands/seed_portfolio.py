from django.core.management.base import BaseCommand

from portfolio.models import (
    Award,
    Education,
    Experience,
    PortfolioProfile,
    Publication,
    ResearchProject,
    Skill,
    SkillCategory,
)


class Command(BaseCommand):
    help = "Add the supplied CV content to an empty portfolio database."

    def handle(self, *args, **options):
        self.seed_profile()
        self.seed_education()
        self.seed_experience()
        self.seed_projects()
        self.seed_publications()
        self.seed_skills()
        self.seed_awards()
        self.stdout.write(self.style.SUCCESS("Portfolio content is ready."))

    def seed_profile(self):
        if PortfolioProfile.objects.exists():
            return
        PortfolioProfile.objects.create(
            name="Mahedi Hasan",
            title="Lecturer",
            department="Department of Computer Science & Engineering",
            institution="International University of Business Agriculture and Technology (IUBAT)",
            location="Dhaka, Bangladesh",
            email="mahedi.cse@iubat.edu",
            phone="+880 1705054376",
            biography=(
                "I am a Lecturer in Computer Science and Engineering at IUBAT, where I teach, "
                "mentor undergraduate researchers, and pursue collaborative research. My work "
                "centers on human-centric computer vision, multimodal learning, and practical "
                "AI methods for healthcare, video understanding, and intelligent transportation."
            ),
            research_interests="\n".join(
                [
                    "Human-Centric Computer Vision",
                    "Spatial-Temporal Video Analytics",
                    "Multi-modal Scene Understanding",
                    "Vision-Language Models",
                    "Interactive Machine Learning (Human-in-the-Loop)",
                    "Medical Image Analysis & Biometrics",
                    "Intelligent Transportation Systems",
                ]
            ),
        )

    def seed_education(self):
        if Education.objects.exists():
            return
        Education.objects.create(
            degree="B.Sc. in Computer Science and Engineering",
            institution="Chittagong University of Engineering and Technology (CUET)",
            location="Chittagong, Bangladesh",
            period="2018–2023",
            result="CGPA: 3.85/4.00 · Ranked 5th out of 120",
            thesis="Multimodal and Physics-Aware Human Fall Detection for Safety-Critical Healthcare Applications",
        )

    def seed_experience(self):
        if Experience.objects.exists():
            return
        Experience.objects.create(
            role="Lecturer, Department of Computer Science and Engineering",
            organization="International University of Business Agriculture and Technology",
            location="Dhaka, Bangladesh",
            period="July 2023–Present",
            summary=(
                "Teach undergraduate computing courses, develop learning and assessment materials, "
                "and advise students on academic progress, research, and career development."
            ),
            highlights="\n".join(
                [
                    "Courses include Data Structures and Algorithms, Data Communications and Computer Networks, Object-Oriented Programming, Computer Vision and Image Processing, Java Programming, Computer Organizations and Architecture, and Computer Graphics.",
                    "Design lectures, laboratory sessions, assignments, projects, and examinations; assess and provide detailed feedback to cohorts of 35–40 students.",
                    "Provide structured academic advising, targeted improvement plans, one-to-one support, and guidance on graduate study, research, and career pathways.",
                ]
            ),
            display_order=1,
        )
        Experience.objects.create(
            role="Competitive Programming Coach & Contest Director",
            organization="IUBAT IT Society",
            location="Dhaka, Bangladesh",
            period="July 2023–Present",
            summary=(
                "Founded and lead the society's competitive programming wing, supporting "
                "algorithmic learning, contest practice, and student research development."
            ),
            highlights="\n".join(
                [
                    "Created a structured learning community and curriculum in algorithms, data structures, problem solving, and contest time management.",
                    "Lead weekly learning sessions and organize regular virtual programming contests.",
                    "Served as problem setter and head of the judge panel for an intra-university programming contest; received a certificate of appreciation from the CSE Department.",
                    "Coach student teams at inter-university contests and support mentees progressing into collaborative research.",
                ]
            ),
            display_order=2,
        )
        Experience.objects.create(
            role="Undergraduate Thesis Supervisor",
            organization="Department of Computer Science and Engineering, IUBAT",
            location="Dhaka, Bangladesh",
            period="2024–Present",
            summary=(
                "Supervise undergraduate research in Bangla sign language recognition, license "
                "plate detection, image captioning, and traffic object detection."
            ),
            highlights="\n".join(
                [
                    "Guided a CNN and Vision Transformer benchmarking framework for 36 Bangla sign classes, reporting 99.54% validation accuracy; published at IEEE QPAIN 2026.",
                    "Supervised YOLOv8 with CBAM for Bangladeshi license plate detection, reporting 98.9% mAP@50 and 32 FPS; published at IEEE QPAIN 2026.",
                    "Guide a Bangla image captioning project combining Vision Transformer and BanglaBERT; manuscript in preparation.",
                    "Guide an attention-enhanced YOLOv11 project for vehicle detection in unstructured Bangladeshi traffic; manuscript in preparation.",
                ]
            ),
            display_order=3,
        )

    def seed_projects(self):
        if ResearchProject.objects.exists():
            return
        projects = [
            {
                "title": "Two-Stage Vision Transformer Framework for Surveillance Video Anomaly Detection",
                "category": "Video analytics",
                "period": "2024–2025",
                "description": "Developed a two-stage CNN–ViT pipeline using keyframe selection to identify anomalous events across UCF-Crime categories.",
                "result": "98% binary and 95% multi-class accuracy; keyframe extraction reduced processing time by 65%.",
                "outcome": "Published · IEEE ECCE 2025",
            },
            {
                "title": "Human-in-the-Loop Vision Transformer for Facial Emotion Recognition",
                "category": "Human-centered AI",
                "period": "2024–2025",
                "description": "Introduced confidence-based human intervention and incremental model updating for emotion recognition across four benchmark datasets.",
                "result": "Reported accuracy gains of 7%, 5%, 10%, and 13% across evaluated datasets; 82.5% on FER2013 and 75.0% on AffectNet-7.",
                "outcome": "Published · IEEE QPAIN 2025",
            },
            {
                "title": "Generative Adversarial Networks for Transaction Anomaly Detection",
                "category": "Synthetic data & fraud detection",
                "period": "2024–2025",
                "description": "Applied a conditional GAN to generate synthetic minority-class transaction samples for an imbalanced credit-card fraud dataset.",
                "result": "99.8% accuracy, 95% precision, 89% recall, 91% F1-score, and 0.98 AUC-ROC.",
                "outcome": "Published · IEEE QPAIN 2025",
            },
            {
                "title": "Multimodal, Physics-Aware Human Fall Detection",
                "category": "Healthcare computer vision",
                "period": "2022–2023",
                "description": "Undergraduate thesis combining human-body structure, scene appearance, and temporal motion; uses biomechanically informed frame selection and GNN–ViT feature fusion.",
                "result": "Evaluated across URFall, Le2i, and Multicamera Fall Detection datasets; manuscript in preparation.",
                "outcome": "Undergraduate thesis",
            },
            {
                "title": "Bangla Sign Language Recognition with CNNs and Transformers",
                "category": "Thesis supervision",
                "period": "2024–Present",
                "description": "Supervised comparative evaluation of ResNet50, VGG16, MobileNetV2, and partially fine-tuned ViT across 36 Bangla letter classes.",
                "result": "99.54% validation accuracy with ViT-Base-Patch16-224.",
                "outcome": "Published · IEEE QPAIN 2026",
            },
            {
                "title": "CBAM-Enhanced Bangladeshi License Plate Detection",
                "category": "Thesis supervision",
                "period": "2024–Present",
                "description": "Supervised YOLOv8 architecture enhancements and ablation studies using the Bangla LPDB-A dataset.",
                "result": "98.9% mAP@50 at 32 FPS on an RTX 3080 GPU.",
                "outcome": "Published · IEEE QPAIN 2026",
            },
            {
                "title": "Bangla Image Captioning with Vision Transformer and BanglaBERT",
                "category": "Thesis supervision",
                "period": "2025–Present",
                "description": "Guiding a multimodal captioning architecture with contrastive pre-alignment and a hybrid decoder for Bangla image descriptions.",
                "result": "BLEU-4 0.5498 · METEOR 0.6488 · ROUGE-L 0.7040 · CIDEr 1.8981.",
                "outcome": "Manuscript in preparation",
            },
            {
                "title": "Attention-Guided YOLOv11 for Unstructured Traffic",
                "category": "Thesis supervision",
                "period": "2024–Present",
                "description": "Guiding a CBAM-integrated YOLOv11m approach to traffic detection in local conditions, with occlusion and diverse vehicle types.",
                "result": "Custom dataset: 265,698 annotated instances across nine vehicle classes; mAP improved from 75.1% to 75.7%.",
                "outcome": "Manuscript in preparation",
            },
        ]
        ResearchProject.objects.bulk_create(
            [ResearchProject(display_order=index, **project) for index, project in enumerate(projects, 1)]
        )

    def seed_publications(self):
        if Publication.objects.exists():
            return
        publications = [
            {
                "title": "A Reproducible Comet-Assay Pipeline: Segmentation, Morphometrics, and Binary Grading with Auditable Ablations",
                "authors": "A. H. Emon, N. Jahan, M. Hasan, F. A. Jibon, S. Mohammad, and A. H. M. Kamal",
                "venue": "Egyptian Journal of Medical Human Genetics (Springer Open)",
                "year": 2026,
                "publication_type": Publication.Type.JOURNAL,
                "status": "Under review",
            },
            {
                "title": "Multi-Architecture Comparative Framework for Bangla Sign Language Classification using CNN and Transformer Models",
                "authors": "M. Hasan, N. Tabassum, S. S. Jese, and M. Tasnim",
                "venue": "IEEE International Conference on Quantum Photonics, Artificial Intelligence, and Networking (QPAIN), Chittagong, Bangladesh",
                "year": 2026,
                "publication_type": Publication.Type.CONFERENCE,
                "status": "Published · Supervising author",
            },
            {
                "title": "Enhanced YOLOv8 with Convolutional Block Attention Module (CBAM) for Real-Time Bangladeshi License Plate Detection",
                "authors": "P. B. Barua, S. N. Lima, and M. Hasan",
                "venue": "IEEE International Conference on Quantum Photonics, Artificial Intelligence, and Networking (QPAIN), Chittagong, Bangladesh",
                "year": 2026,
                "publication_type": Publication.Type.CONFERENCE,
                "status": "Published · Supervising author",
            },
            {
                "title": "Enhancing Face-to-Emotion Recognition with Vision Transformer and Human-in-the-Loop Approach",
                "authors": "M. Hasan, N. I. Shuvo, A. Akter, F. S. Tamim, N. Ahmed, N. Mia, and S. Alam",
                "venue": "IEEE International Conference on Quantum Photonics, Artificial Intelligence, and Networking (QPAIN), Rangpur, Bangladesh",
                "year": 2025,
                "publication_type": Publication.Type.CONFERENCE,
                "status": "Published · First author",
                "doi_url": "https://doi.org/10.1109/QPAIN66474.2025.11171658",
            },
            {
                "title": "Two-Stage Vision Transformer-Based Framework for Anomaly Detection and Classification in Surveillance Videos",
                "authors": "M. Hasan, J. A. Nabin, N. Mia, F. S. Tamim, S. Mohammad, and D. M. Das",
                "venue": "IEEE International Conference on Electrical, Computer and Communication Engineering (ECCE), Chittagong, Bangladesh",
                "year": 2025,
                "publication_type": Publication.Type.CONFERENCE,
                "status": "Published · First author",
                "doi_url": "https://doi.org/10.1109/ECCE64574.2025.11013374",
            },
            {
                "title": "Generative Adversarial Networks for Transaction Anomaly Detection: A Synthetic Data Approach",
                "authors": "M. Hasan, K. N. Hasan, F. S. Tamim, M. S. Arefin, and A. W. Reza",
                "venue": "IEEE International Conference on Quantum Photonics, Artificial Intelligence, and Networking (QPAIN), Rangpur, Bangladesh",
                "year": 2025,
                "publication_type": Publication.Type.CONFERENCE,
                "status": "Published · First author",
                "doi_url": "https://doi.org/10.1109/QPAIN66474.2025.11172003",
            },
            {
                "title": "Association Rule Mining for Analyzing User Listening Patterns and Performance",
                "authors": "F. S. Tamim, Z. S. Taheri, M. Hasan, M. S. Arefin, A. W. Reza, and Z. S. Taheri",
                "venue": "IEEE International Conference on Quantum Photonics, Artificial Intelligence, and Networking (QPAIN), Rangpur, Bangladesh",
                "year": 2025,
                "publication_type": Publication.Type.CONFERENCE,
                "status": "Published",
                "doi_url": "https://doi.org/10.1109/QPAIN66474.2025.11171825",
            },
            {
                "title": "A Comparative Study of Machine Learning Models for Air Quality Index Classification in Urban Bangladesh",
                "authors": "M. S. R. Pk., M. Hasan, M. S. Arefin, A. W. Reza, F. S. Tamim, and Z. S. Taheri",
                "venue": "IEEE International Conference on Electrical, Computer and Communication Engineering (ECCE), Chittagong, Bangladesh",
                "year": 2025,
                "publication_type": Publication.Type.CONFERENCE,
                "status": "Published",
                "doi_url": "https://doi.org/10.1109/ECCE64574.2025.11013895",
            },
            {
                "title": "Federated Deep Learning for Cybersecurity and Intrusion Detection in Decentralized Networks",
                "authors": "N. Mia, J. A. Nabin, S. Mohammad, M. Hasan, F. S. Tamim, and D. M. Das",
                "venue": "International Conference on Advancements in Electrical, Electronics, Communication, Computing and Automation (ICAECA), Coimbatore, India",
                "year": 2025,
                "publication_type": Publication.Type.CONFERENCE,
                "status": "Published",
                "doi_url": "https://doi.org/10.1109/ICAECA63854.2025.11012607",
            },
            {
                "title": "A New Approach to Solve Job Sequencing Problem Using Dynamic Programming with Reduced Time Complexity",
                "authors": "T. Ahammad, M. Hasan, M. Hasan, M. S. Hossain, A. Hoque, and M. M. Rashid",
                "venue": "Computing Science, Communication and Security (COMS2), Communications in Computer and Information Science, vol. 1235, Springer, Singapore, pp. 316–327",
                "year": 2020,
                "publication_type": Publication.Type.BOOK_CHAPTER,
                "status": "Published",
                "doi_url": "https://doi.org/10.1007/978-981-15-6648-6_25",
            },
        ]
        Publication.objects.bulk_create(
            [Publication(display_order=index, **publication) for index, publication in enumerate(publications, 1)]
        )

    def seed_skills(self):
        if SkillCategory.objects.exists():
            return
        groups = {
            "Programming & Databases": ["Python", "C++", "MATLAB", "MySQL", "MongoDB"],
            "AI & Machine Learning": ["PyTorch", "TensorFlow", "Keras", "Scikit-learn", "NumPy", "Pandas", "Matplotlib", "Tableau"],
            "Web Technologies": ["Angular", "Next.js", "Node.js", "Django"],
            "Tools & Platforms": ["Jupyter Notebook", "Google Colab", "Kaggle", "LaTeX", "Cisco Packet Tracer"],
        }
        for category_order, (name, skills) in enumerate(groups.items(), 1):
            category = SkillCategory.objects.create(name=name, display_order=category_order)
            Skill.objects.bulk_create(
                [
                    Skill(category=category, name=skill, display_order=index)
                    for index, skill in enumerate(skills, 1)
                ]
            )

    def seed_awards(self):
        if Award.objects.exists():
            return
        awards = [
            (
                "Miyan Research Institute Award for Faculty Excellence",
                "IUBAT",
                "2026",
                "Recognized for outstanding research productivity, comprising six peer-reviewed journal publications within two years of joining as faculty.",
            ),
            (
                "Bachelor of Science with Honors",
                "Chittagong University of Engineering and Technology",
                "2023",
                "Graduated with CGPA 3.85/4.00, ranking 5th among 120 students in the department.",
            ),
            (
                "Dean’s List Award",
                "Chittagong University of Engineering and Technology",
                "2020–2023",
                "Awarded for three consecutive academic years in recognition of sustained academic excellence (GPA ≥ 3.75 each semester).",
            ),
            (
                "First Place, National Science Olympiad",
                "Government of Bangladesh",
                "2017",
                "38th National Science & Technology Week, organized by the Ministry of Science & Technology.",
            ),
            (
                "Government Merit Scholarships",
                "Education Ministry, Bangladesh",
                "2010, 2013, 2016",
                "Awarded at three levels of national examination (PSC, JSC, and SSC) based on academic merit; ranked first in Gopalganj District at JSC.",
            ),
        ]
        Award.objects.bulk_create(
            [
                Award(
                    title=title,
                    organization=organization,
                    year=year,
                    details=details,
                    display_order=index,
                )
                for index, (title, organization, year, details) in enumerate(awards, 1)
            ]
        )
