import re

candidates = {
    "TCONS_00004856",
    "TCONS_00004857",
    "TCONS_00004858",
    "TCONS_00008053",
    "TCONS_00008054",
    "TCONS_00025093",
    "TCONS_00026006",
    "TCONS_00026007",
}

print("Transcript\tGene\tSample\tCoverage\tFPKM\tTPM")

with open("gffcompare/WFA_compare_final.tracking") as f:
    for line in f:
        if not any(t in line for t in candidates):
            continue

        fields = line.rstrip().split("\t")
        transcript = fields[0].split("|")[0]
        gene = fields[1]

        for field in fields[4:]:
            if field == "-" or field.strip() == "":
                continue

            m = re.match(
                r"(q\d+):[^|]+\|[^|]+\|\d+\|([\d.]+)\|([\d.]+)\|([\d.]+)\|",
                field,
            )

            if m:
                sample = m.group(1)
                cov = m.group(2)
                fpkm = m.group(3)
                tpm = m.group(4)
                print(f"{transcript}\t{gene}\t{sample}\t{cov}\t{fpkm}\t{tpm}")
