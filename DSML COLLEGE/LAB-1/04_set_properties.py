"""
LAB 1 - Part 2.3: Explore Set Properties in Python
Topics Covered:
1. Unique elements property (automatic deduplication).
2. Unordered nature and index-less structure.
3. Fast O(1) membership testing using hash tables.
4. Set modification: add(), update(), remove(), discard(), pop(), clear().
5. Mathematical Set Operations:
   - Union (| or union())
   - Intersection (& or intersection())
   - Difference (- or difference())
   - Symmetric Difference (^ or symmetric_difference())
6. Subset, superset, and disjoint relationships.
7. Practical application: Removing duplicate data samples in ML workflows.
"""

print("=" * 80)
print("LAB 1 - PART 2.3: EXPLORING PYTHON SET PROPERTIES")
print("=" * 80)

# 1. Uniqueness Property
raw_student_ids = [101, 102, 105, 101, 103, 102, 104, 105, 106, 101]
unique_ids = set(raw_student_ids)

print(f"Raw Input with duplicates ({len(raw_student_ids)} items): {raw_student_ids}")
print(f"Set (Deduplicated, {len(unique_ids)} items): {unique_ids}")

# 2. Unordered Nature
names_set = {"Python", "NumPy", "Pandas", "PyTorch", "Scikit-Learn"}
print(f"\nSet elements: {names_set}")
print("Note: Sets do not maintain insertion order and cannot be indexed like names_set[0].")

# 3. O(1) Membership Testing
query = "PyTorch"
print(f"\nIs '{query}' in set? {'Yes' if query in names_set else 'No'}")

# 4. Modifying Sets
print("\n--- Modifying Sets ---")
names_set.add("Matplotlib")
print(f"After add('Matplotlib'): {names_set}")

names_set.update(["Seaborn", "SciPy"])
print(f"After update(['Seaborn', 'SciPy']): {names_set}")

# remove() vs discard()
names_set.remove("SciPy")  # Raises KeyError if not found
print(f"After remove('SciPy'): {names_set}")

names_set.discard("NonExistentLib")  # Safe: does not raise error if not found
print("discard('NonExistentLib') succeeded safely without exception.")

# 5. Mathematical Set Operations
print("\n--- Mathematical Set Operations ---")
ds_skills = {"Python", "SQL", "Machine Learning", "Statistics", "Pandas"}
web_skills = {"Python", "JavaScript", "HTML", "CSS", "SQL"}

print(f"Set A (Data Science Skills): {ds_skills}")
print(f"Set B (Web Dev Skills):      {web_skills}")

# Union: A | B (All unique elements across both sets)
union_skills = ds_skills | web_skills
print(f"\nUnion (A | B) -> Total Unique Skills: {union_skills}")

# Intersection: A & B (Elements common to both sets)
common_skills = ds_skills & web_skills
print(f"Intersection (A & B) -> Common Skills: {common_skills}")

# Difference: A - B (Elements in A but not in B)
ds_exclusive = ds_skills - web_skills
print(f"Difference (A - B) -> Exclusive to DS: {ds_exclusive}")

# Difference: B - A (Elements in B but not in A)
web_exclusive = web_skills - ds_skills
print(f"Difference (B - A) -> Exclusive to Web: {web_exclusive}")

# Symmetric Difference: A ^ B (Elements in either A or B, but NOT both)
either_not_both = ds_skills ^ web_skills
print(f"Symmetric Difference (A ^ B): {either_not_both}")

# 6. Relational Predicates
print("\n--- Set Relations ---")
subset_test = {"Python", "SQL"}
print(f"Is {subset_test} a subset of DS skills? {subset_test.issubset(ds_skills)}")
print(f"Is DS skills a superset of {subset_test}? {ds_skills.issuperset(subset_test)}")

unrelated = {"C++", "Rust"}
print(f"Are {unrelated} and DS skills disjoint (no common items)? {unrelated.isdisjoint(ds_skills)}")

# 7. Practical ML Example: Vocabulary Extraction from text corpus
print("\n--- Practical ML Example: Vocabulary Builder ---")
documents = [
    "deep learning models require large datasets",
    "machine learning and deep learning are transformative",
    "python is great for machine learning"
]
vocab = set()
for doc in documents:
    words = doc.lower().split()
    vocab.update(words)

print(f"Text Corpus ({len(documents)} sentences)")
print(f"Vocabulary Size (Unique tokens): {len(vocab)}")
print(f"Unique Vocabulary: {sorted(list(vocab))}")
print("=" * 80)
