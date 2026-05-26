from pybtex.database.input import bibtex


def get_personal_data():
    name = ["Stefano", "Esposito"]
    bio_text = f"""
                <p>I am a PhD student at the <a href="https://uni-tuebingen.de/en/">University of Tübingen</a>, part of <a href="https://uni-tuebingen.de/en/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/autonomous-vision/home/">Autonomous Vision Group</a> headed by <a href="https://www.cvlibs.net/">Prof. Andreas Geiger</a>.</p>
                <p>
                    <span style="font-weight: bold;">Research:</span>
                    I am particularly interested in 3D computer vision topics leveraging coordinate-based neural networks (neural fields). Such methods parameterize the physical properties of scenes or objects in space and time, and have been successfully applied to problems such as novel view synthesis, 3D reconstruction, pose estimation and animations.
                </p>
                <p>
                    <span style="font-weight: bold;">Bio:</span> 
                    I've obtained a bachelor's degree in computer science and a master's degree in "artificial intelligence and robotics" at the <a href="https://www.uniroma1.it/en/pagina-strutturale/home">University of Rome "La Sapienza"</a>. During and after my master I have been an Erasmus student and a full-time research associate at the <a href="https://www.h-brs.de/en">Hochschule Bonn-Rhein-Sieg</a> in Bonn, Germany. I see myself as an educated programmer and a true technology enthusiast; in my spare time I enjoy learning new things, traveling, and keeping up to date with what is happening in the world. I love connecting with nature by hiking in the mountains. 
                </p>
                <p>For any inquiries, feel free to reach out!</p>
                <p class="social-links">
                    <a href="https://s-esposito.github.io/assets/pdf/Stefano_Esposito_CV.pdf" target="_blank"><i class="fa fa-address-card fa-lg"></i> CV</a>
                    <a href="mailto:stefano.esposito97@outlook.com"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://bsky.app/profile/s-esposito.bsky.social" target="_blank"><i class="fa-brands fa-bluesky"></i> Bluesky</a>
                    <a href="https://x.com/StefanoEsp" target="_blank"><i class="fa-brands fa-x-twitter"></i> Twitter</a>
                    <a href="https://scholar.google.com/citations?user=5RhJ-eEAAAAJ&hl=it" target="_blank"><i class="fa-solid fa-book"></i> Scholar</a>
                    <a href="https://github.com/s-esposito" target="_blank"><i class="fab fa-github fa-lg"></i> Github</a>
                    <a href="https://www.linkedin.com/in/stefanoesposito97" target="_blank"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                </p>
    """
    footer = """
            <div class="col-sm-12 footer-credits">
                <p>
                    Website template provided by <a href="https://github.com/m-niemeyer/m-niemeyer.github.io" target="_blank">Michael Niemeyer</a>. <br>
                    <a href="https://m-niemeyer.github.io/" target="_blank">&#9883;</a>
                    <a href="https://kashyap7x.github.io/" target="_blank">&#9883;</a>
                    <a href="https://kait0.github.io/" target="_blank">&#9883;</a>
                </p>
            </div>
    """
    return name, bio_text, footer


def get_author_dict():
    return {
        "Andreas Geiger": "https://www.cvlibs.net/",
        "Songyou Peng": "https://pengsongyou.github.io/",
        "Zehao Yu": "https://niujinshuchong.github.io/",
        "Torsten Sattler": "https://tsattler.github.io/",
        "Katja Schwarz": "https://katjaschwarz.github.io/",
        "Axel Sauer": "https://axelsauer.com/",
        "Jonathan Barron": "https://jonbarron.info/",
        "Ben Mildenhall": "https://bmild.github.io/",
        "Mehdi Sajjadi": "https://msajjadi.com/",
        "Noha Radwan": "http://www2.informatik.uni-freiburg.de/~radwann/",
        "Chiyu Jiang": "https://www.maxjiang.ml/",
        "Yiyi Liao": "https://yiyiliao.github.io/",
        "Marc Pollefeys": "https://people.inf.ethz.ch/pomarc/",
        "Michael Oechsle": "https://moechsle.github.io/",
        "Christian Reiser": "https://creiser.github.io/",
        "Lars Mescheder": "https://scholar.google.de/citations?user=h2k1gL4AAAAJ&hl=de",
        "Thilo Strauss": "https://scholar.google.com/citations?user=VlymtLQAAAAJ&hl=en",
        "Sebastian Nowozin": "http://www.nowozin.net/sebastian/",
        "Marie-Julie Rakotosaona": "http://www.lix.polytechnique.fr/Labo/Marie-Julie.RAKOTOSAONA/",
        "Fabian Manhardt": "https://campar.in.tum.de/Main/FabianManhardt",
        "Diego Martin Arroyo": "https://martinarroyo.net/",
        "Abhijit Kundu": "https://abhijitkundu.info/",
        "Federico Tombari": "https://www.cs.cit.tum.de/camp/members/senior-research-scientists/federico-tombari/",
        "Anpei Chen": "https://apchenstu.github.io/",
        "Bozidar Antic": "https://bozidarantic.com/",
        "Apratim Bhattacharyya": "https://apratimbhattacharyya18.github.io/",
        "Siyu Tang": "https://inf.ethz.ch/people/person-detail.MjYyNzgw.TGlzdC8zMDQsLTg3NDc3NjI0MQ==.html",
        "Daniele Baieri": "https://gladia.di.uniroma1.it/authors/baieri/",
        "Stefan Zellmann": "https://www.szellmann.de/",
        "André Hinkenjann": "https://www.h-brs.de/en/inf/prof-dr-andre-hinkenjann",
        "Emanuele Rodolà": "https://gladia.di.uniroma1.it/authors/rodola/",
        "Filippo Maggioli": "https://gladia.di.uniroma1.it/authors/maggioli/",
        "Samuel Rota Bulò": "https://scholar.google.com/citations?user=484sccEAAAAJ&hl=it",
        "Lorenzo Porzi": "https://scholar.google.it/citations?user=vW1gaVEAAAAJ&hl=it",
        "Christian Richardt": "https://richardt.name/",
        "Michael Zollhoefer": "https://zollhoefer.com/",
        "Peter Kontschieder": "https://scholar.google.co.uk/citations?user=CxbDDRMAAAAJ&hl=en",
        "Haofei Xu": "https://haofeixu.github.io/",
        "Siyu Tang": "https://inf.ethz.ch/people/person-detail.MjYyNzgw.TGlzdC8zMDQsLTg3NDc3NjI0MQ==.html",
        "Donato Crisostomi": "https://crisostomi.com/",
    }


def generate_person_html(
    persons,
    connection=", ",
    highlight=True,
    highlight_name="Stefano Esposito",
    add_links=True,
):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        plain_name = ""
        for name_part_i in p.get_part("first") + p.get_part("last"):
            if plain_name != "":
                plain_name += " "
            plain_name += name_part_i
        if plain_name in links.keys():
            string_part_i = (
                f'<a href="{links[plain_name]}" target="_blank">{plain_name}</a>'
            )
        else:
            string_part_i = plain_name
        if highlight and plain_name == highlight_name:
            string_part_i = f'<span style="font-style: italic;">{string_part_i}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s


def get_paper_entry(entry_key, entry):
    s = """<div class="publication-card"><div class="row"><div class="col-4 col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid custom-img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-8 col-sm-9">"""

    if "html" in entry.fields.keys():
        title_html = f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a>"""
    else:
        title_html = entry.fields["title"]
    if "award" in entry.fields.keys():
        s += f"""{title_html} <span class="award">({entry.fields['award']})</span><br>"""
    else:
        s += f"""{title_html} <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    if "booktitle" in entry.fields.keys():
        s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']}"""
    elif "note" in entry.fields.keys():
        s += f"""<span style="font-style: italic;">{entry.fields['note']}</span>, {entry.fields['year']}"""
    else:
        s += f"""{entry.fields['year']}"""

    artefacts = {
        "html": ("Project Page", "fa-solid fa-globe"),
        "pdf": ("Paper", "fa-solid fa-file-pdf"),
        "supp": ("Supplemental", "fa-solid fa-paperclip"),
        "video": ("Video", "fa-solid fa-video"),
        "poster": ("Poster", "fa-solid fa-image"),
        "code": ("Code", "fa-brands fa-github"),
    }
    links = []
    for k, (label, icon) in artefacts.items():
        if k in entry.fields.keys():
            links.append(
                f'<a href="{entry.fields[k]}" target="_blank"><i class="{icon}"></i> {label}</a>'
            )

    cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    cite += (
        "\tauthor = {"
        + f"{generate_person_html(entry.persons['author'], highlight=False, add_links=False, connection=' and ')}"
        + "}, \n"
    )
    if "booktitle" in entry.fields.keys():
        cite += "\tbooktitle = " + "{" + f"{entry.fields['booktitle']}" + "}, \n"
    if "note" in entry.fields.keys():
        cite += "\tnote = " + "{" + f"{entry.fields['note']}" + "}, \n"
    for entr in ["title", "year"]:
        cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""

    bibtex_button = f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapse{entry_key}"><i class="fa-solid fa-quote-right"></i> Bibtex</button>"""
    s += f"""<div class="publication-links">{' '.join(links)}{bibtex_button}</div>"""
    s += f"""<div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """</div></div></div>"""
    return s


def get_talk_entry(entry_key, entry):
    s = """<div class="publication-card"><div class="row"><div class="col-4 col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid custom-img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-8 col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']}"""

    artefacts = {
        "slides": ("Slides", "fa-solid fa-file-powerpoint"),
        "video": ("Recording", "fa-solid fa-video"),
    }
    links = []
    for k, (label, icon) in artefacts.items():
        if k in entry.fields.keys():
            links.append(
                f'<a href="{entry.fields[k]}" target="_blank"><i class="{icon}"></i> {label}</a>'
            )
    if links:
        s += f"""<div class="publication-links">{' '.join(links)}</div>"""
    s += """</div></div></div>"""
    return s


def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file("publication_list.bib")
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s += get_paper_entry(k, bib_data.entries[k])
    return s


def get_talks_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file("talk_list.bib")
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s += get_talk_entry(k, bib_data.entries[k])
    return s


def get_index_html():
    pub = get_publications_html()
    talks = get_talks_html()
    name, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
    <html lang="en">

    <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-JLDH01R2DE"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());

    gtag('config', 'G-JLDH01R2DE');
    </script>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <!-- Custom CSS -->
    <link rel="stylesheet" href="assets/css/style.css">

    <!-- Theme init: applied before paint to avoid flash of wrong theme -->
    <script>
    (function() {{
        try {{
            var saved = localStorage.getItem('theme');
            if (saved === 'light' || saved === 'dark') {{
                document.documentElement.setAttribute('data-theme', saved);
            }}
        }} catch (e) {{}}
    }})();
    </script>

    <title>{name[0] + ' ' + name[1]}</title>
    <link rel="icon" type="image/x-icon" href="assets/favicon.ico">
    </head>

    <body>
        <button id="theme-toggle" class="theme-toggle" type="button" aria-label="Toggle color theme" title="Toggle color theme">
            <i class="fa-solid fa-circle-half-stroke"></i>
        </button>
        <div class="container">
            <div class="row" style="margin-top: 3em;">
                <div class="col-sm-12" style="margin-bottom: 2em;">
                <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
                </div>
                <br>
                <div class="col-md-8" style="">
                    {bio_text}
                </div>
                <div class="col-md-4">
                    <img src="assets/img/profile.jpg" class="custom-img-thumbnail profile-photo" alt="Profile picture">
                </div>
            </div>
            <div class="row" style="margin-top: 2em;">
                <div class="col-sm-12" style="">
                    <h4>Publications</h4>
                    {pub}
                </div>
            </div>
            <!--
            <div class="row" style="margin-top: 3em;">
                <div class="col-sm-12" style="">
                    <h4>Talks</h4>
                    {talks}
                </div>
            </div>
            -->
            <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
                {footer}
            </div>
        </div>

        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>

        <!-- Theme toggle: cycles auto (OS) -> light -> dark -> auto -->
        <script>
        (function() {{
            var btn = document.getElementById('theme-toggle');
            if (!btn) return;
            var root = document.documentElement;
            var ICONS = {{
                auto: '<i class="fa-solid fa-circle-half-stroke"></i>',
                light: '<i class="fa-solid fa-sun"></i>',
                dark: '<i class="fa-solid fa-moon"></i>'
            }};
            var LABELS = {{
                auto: 'Theme: follows system. Click to switch to light.',
                light: 'Theme: light. Click to switch to dark.',
                dark: 'Theme: dark. Click to follow system.'
            }};
            function getState() {{
                try {{
                    var v = localStorage.getItem('theme');
                    if (v === 'light' || v === 'dark') return v;
                }} catch (e) {{}}
                return 'auto';
            }}
            function applyState(state) {{
                if (state === 'auto') {{
                    root.removeAttribute('data-theme');
                    try {{ localStorage.removeItem('theme'); }} catch (e) {{}}
                }} else {{
                    root.setAttribute('data-theme', state);
                    try {{ localStorage.setItem('theme', state); }} catch (e) {{}}
                }}
                btn.innerHTML = ICONS[state];
                btn.setAttribute('aria-label', LABELS[state]);
                btn.setAttribute('title', LABELS[state]);
            }}
            applyState(getState());
            btn.addEventListener('click', function() {{
                var current = getState();
                var next = current === 'auto' ? 'light' : current === 'light' ? 'dark' : 'auto';
                applyState(next);
            }});
        }})();
        </script>
    </body>

    </html>
    """
    return s


def write_index_html(filename="index.html"):
    s = get_index_html()
    with open(filename, "w", encoding="utf-8") as f:
        f.write(s)
    print(f"Written index content to {filename}.")


if __name__ == "__main__":
    write_index_html("index.html")
