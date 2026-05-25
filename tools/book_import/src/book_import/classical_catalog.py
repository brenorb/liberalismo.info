from __future__ import annotations

from copy import deepcopy


def ebook_page(ebook_id: int) -> str:
    return f"https://www.gutenberg.org/ebooks/{ebook_id}"


def ebook_text(ebook_id: int) -> str:
    return f"https://www.gutenberg.org/ebooks/{ebook_id}.txt.utf-8"


def work(
    *,
    title: str,
    slug: str,
    author_key: str,
    year: int,
    original_language: str,
    ebook_id: int | None = None,
    source_url: str | None = None,
    source_text_url: str | None = None,
    tags: list[str],
    excerpt: str,
    mode: str = "fulltext",
) -> dict[str, object]:
    page_url = f"/library/{slug}/"
    resolved_source_url = source_url or (ebook_page(ebook_id) if ebook_id is not None else "")
    resolved_source_text_url = source_text_url or (ebook_text(ebook_id) if ebook_id is not None else "")
    return {
        "title": title,
        "slug": slug,
        "url": page_url,
        "author_key": author_key,
        "year_first_published": year,
        "original_language": original_language,
        "source_url": resolved_source_url,
        "source_text_url": resolved_source_text_url,
        "tags": tags,
        "excerpt": excerpt,
        "mode": mode,
    }


AUTHORS: list[dict[str, str]] = [
    {
        "key": "adam-smith",
        "name": "Adam Smith",
        "slug": "adam-smith",
        "subtitle": "Scottish moral philosopher and political economist",
        "bio": "Adam Smith (1723-1790) connected moral psychology, commercial society, and political economy in ways that became foundational for classical liberal thought.",
        "bio_pt_br": "Adam Smith (1723-1790) conectou psicologia moral, sociedade comercial e economia politica de modo decisivo para o liberalismo classico.",
    },
    {
        "key": "alexis-de-tocqueville",
        "name": "Alexis de Tocqueville",
        "slug": "alexis-de-tocqueville",
        "subtitle": "French analyst of democracy, civil society, and centralization",
        "bio": "Alexis de Tocqueville (1805-1859) studied democracy as a social condition, pairing admiration for self-government with warnings about centralization and majority pressure.",
        "bio_pt_br": "Alexis de Tocqueville (1805-1859) estudou a democracia como condicao social, admirando o autogoverno e alertando contra centralizacao e tirania da maioria.",
    },
    {
        "key": "david-hume",
        "name": "David Hume",
        "slug": "david-hume",
        "subtitle": "Scottish philosopher, essayist, and historian",
        "bio": "David Hume (1711-1776) brought skepticism, moral psychology, and institutional realism into debates that deeply shaped liberal political thought.",
        "bio_pt_br": "David Hume (1711-1776) levou ceticismo, psicologia moral e realismo institucional a debates que marcaram o pensamento liberal.",
    },
    {
        "key": "f-a-hayek",
        "name": "F. A. Hayek",
        "slug": "f-a-hayek",
        "subtitle": "Austrian-British theorist of spontaneous order and rule-based liberty",
        "bio": "F. A. Hayek (1899-1992) defended dispersed knowledge, spontaneous order, and constitutional limits against comprehensive planning.",
        "bio_pt_br": "F. A. Hayek (1899-1992) defendeu conhecimento disperso, ordem espontanea e limites constitucionais contra o planejamento abrangente.",
    },
    {
        "key": "frederic-bastiat",
        "name": "Frederic Bastiat",
        "slug": "frederic-bastiat",
        "subtitle": "French classical liberal economist and polemic writer",
        "bio": "Frederic Bastiat (1801-1850) wrote concise and durable arguments on law, free exchange, protectionism, and the seen and unseen effects of public policy.",
        "bio_pt_br": "Frederic Bastiat (1801-1850) escreveu argumentos concisos e duradouros sobre lei, troca livre, protecionismo e efeitos vistos e nao vistos das politicas publicas.",
    },
    {
        "key": "herbert-spencer",
        "name": "Herbert Spencer",
        "slug": "herbert-spencer",
        "subtitle": "English individualist theorist of evolution, ethics, and the limits of the state",
        "bio": "Herbert Spencer (1820-1903) linked social evolution, individual liberty, and skepticism toward state overreach in a strongly individualist liberal register.",
        "bio_pt_br": "Herbert Spencer (1820-1903) articulou evolucao social, liberdade individual e ceticismo quanto a expansao estatal em um registro liberal fortemente individualista.",
    },
    {
        "key": "john-locke",
        "name": "John Locke",
        "slug": "john-locke",
        "subtitle": "English philosopher of natural rights and limited government",
        "bio": "John Locke (1632-1704) remains central to liberal accounts of consent, rights, property, toleration, and the justified limits of political power.",
        "bio_pt_br": "John Locke (1632-1704) segue central para concepcoes liberais de consentimento, direitos, propriedade, tolerancia e limites legitimos do poder politico.",
    },
    {
        "key": "john-stuart-mill",
        "name": "John Stuart Mill",
        "slug": "john-stuart-mill",
        "subtitle": "English liberal philosopher of liberty, individuality, and reform",
        "bio": "John Stuart Mill (1806-1873) expanded liberal arguments on individuality, speech, representative institutions, political economy, and social reform.",
        "bio_pt_br": "John Stuart Mill (1806-1873) ampliou os argumentos liberais sobre individualidade, liberdade de expressao, instituicoes representativas, economia politica e reforma social.",
    },
]


WORKS: list[dict[str, object]] = [
    work(title="The Law (A Lei)", slug="the-law", author_key="frederic-bastiat", year=1850, original_language="fr", ebook_id=44800, tags=["liberalism", "economics", "law", "state"], excerpt="Bastiat's classic defense of law as protection of person, liberty, and property."),
    work(title="Economic Sophisms", slug="economic-sophisms", author_key="frederic-bastiat", year=1845, original_language="fr", ebook_id=44145, tags=["liberalism", "economics", "free-trade"], excerpt="A collection of anti-protectionist arguments aimed at common economic fallacies."),
    work(title="Harmonies of Political Economy", slug="harmonies-of-political-economy", author_key="frederic-bastiat", year=1850, original_language="fr", ebook_id=45002, tags=["economics", "liberalism", "markets"], excerpt="Bastiat's longer argument for social cooperation through exchange and spontaneous coordination."),
    work(title="Essays on Political Economy", slug="essays-on-political-economy", author_key="frederic-bastiat", year=1848, original_language="fr", ebook_id=15962, tags=["economics", "liberalism", "state"], excerpt="Short essays on state action, exchange, taxation, and economic reasoning."),
    work(title="Sophisms of the Protectionists", slug="sophisms-of-the-protectionists", author_key="frederic-bastiat", year=1846, original_language="fr", ebook_id=20161, tags=["free-trade", "liberalism", "protectionism"], excerpt="A focused attack on the arguments used to justify tariffs and industrial privilege."),
    work(title="What Is Free Trade?", slug="what-is-free-trade", author_key="frederic-bastiat", year=1845, original_language="fr", ebook_id=16106, tags=["free-trade", "liberalism", "economics"], excerpt="Bastiat's accessible explanation of what free trade means in practical and moral terms."),
    work(title="Protection and Communism", slug="protection-and-communism", author_key="frederic-bastiat", year=1850, original_language="fr", ebook_id=44144, tags=["liberalism", "protectionism", "state"], excerpt="A polemical essay connecting protectionist privilege to broader anti-liberal politics."),
    work(title="Oeuvres Completes de Frederic Bastiat, tome 1", slug="oeuvres-completes-bastiat-tome-1", author_key="frederic-bastiat", year=1854, original_language="fr", ebook_id=35390, tags=["classical-liberalism", "economics", "free-trade"], excerpt="Collected writings from Bastiat's first posthumous French volume."),
    work(title="Oeuvres Completes de Frederic Bastiat, tome 2", slug="oeuvres-completes-bastiat-tome-2", author_key="frederic-bastiat", year=1854, original_language="fr", ebook_id=42300, tags=["classical-liberalism", "economics", "law"], excerpt="Collected writings from Bastiat's second posthumous French volume."),
    work(title="Oeuvres Completes de Frederic Bastiat, tome 3", slug="oeuvres-completes-bastiat-tome-3", author_key="frederic-bastiat", year=1854, original_language="fr", ebook_id=43315, tags=["classical-liberalism", "economics", "state"], excerpt="Collected writings from Bastiat's third posthumous French volume."),
    work(title="Oeuvres Completes de Frederic Bastiat, tome 4", slug="oeuvres-completes-bastiat-tome-4", author_key="frederic-bastiat", year=1855, original_language="fr", ebook_id=46625, tags=["classical-liberalism", "economics", "politics"], excerpt="Collected writings from Bastiat's fourth posthumous French volume."),
    work(title="Oeuvres Completes de Frederic Bastiat, tome 5", slug="oeuvres-completes-bastiat-tome-5", author_key="frederic-bastiat", year=1855, original_language="fr", ebook_id=46626, tags=["classical-liberalism", "economics", "liberty"], excerpt="Collected writings from Bastiat's fifth posthumous French volume."),
    work(title="Oeuvres Completes de Frederic Bastiat, tome 6", slug="oeuvres-completes-bastiat-tome-6", author_key="frederic-bastiat", year=1855, original_language="fr", ebook_id=46627, tags=["classical-liberalism", "economics", "public-policy"], excerpt="Collected writings from Bastiat's sixth posthumous French volume."),
    work(title="Oeuvres Completes de Frederic Bastiat, tome 7", slug="oeuvres-completes-bastiat-tome-7", author_key="frederic-bastiat", year=1855, original_language="fr", ebook_id=46628, tags=["classical-liberalism", "economics", "institutions"], excerpt="Collected writings from Bastiat's seventh posthumous French volume."),
    work(title="On Liberty", slug="on-liberty", author_key="john-stuart-mill", year=1859, original_language="en", ebook_id=34901, tags=["liberalism", "freedom", "individual-rights"], excerpt="Mill's defense of individuality, free expression, and the harm principle."),
    work(title="A System of Logic, Ratiocinative and Inductive", slug="a-system-of-logic", author_key="john-stuart-mill", year=1843, original_language="en", ebook_id=27942, tags=["liberalism", "knowledge", "method"], excerpt="Mill's major work on logic, induction, and the methods of inquiry."),
    work(title="The Subjection of Women", slug="the-subjection-of-women", author_key="john-stuart-mill", year=1869, original_language="en", ebook_id=27083, tags=["liberalism", "equality", "women"], excerpt="Mill argues that legal and social subordination of women is incompatible with justice and liberty."),
    work(title="Utilitarianism", slug="utilitarianism", author_key="john-stuart-mill", year=1863, original_language="en", ebook_id=11224, tags=["liberalism", "ethics", "utilitarianism"], excerpt="A compact statement of Mill's moral theory and its relation to higher pleasures."),
    work(title="Considerations on Representative Government", slug="considerations-on-representative-government", author_key="john-stuart-mill", year=1861, original_language="en", ebook_id=5669, tags=["democracy", "institutions", "liberalism"], excerpt="Mill on representative institutions, political competence, and the design of self-government."),
    work(title="Principles of Political Economy", slug="principles-of-political-economy", author_key="john-stuart-mill", year=1848, original_language="en", ebook_id=30107, tags=["economics", "liberalism", "political-economy"], excerpt="Mill's wide-ranging synthesis of production, distribution, exchange, and reform."),
    work(title="Autobiography", slug="autobiography-of-john-stuart-mill", author_key="john-stuart-mill", year=1873, original_language="en", ebook_id=10378, tags=["biography", "intellectual-history", "liberalism"], excerpt="Mill's account of his education, intellectual formation, and political commitments."),
    work(title="Auguste Comte and Positivism", slug="auguste-comte-and-positivism", author_key="john-stuart-mill", year=1865, original_language="en", ebook_id=16833, tags=["liberalism", "science", "social-theory"], excerpt="Mill's critique and partial engagement with Comte's positivist social philosophy."),
    work(title="Socialism", slug="socialism-by-john-stuart-mill", author_key="john-stuart-mill", year=1879, original_language="en", ebook_id=38138, tags=["liberalism", "socialism", "political-economy"], excerpt="Mill's late reflections on socialist proposals, cooperation, and the limits of reform."),
    work(title="The Contest in America", slug="the-contest-in-america", author_key="john-stuart-mill", year=1862, original_language="en", ebook_id=5123, tags=["america", "democracy", "liberalism"], excerpt="Mill's intervention on the American conflict and its political-moral stakes."),
    work(title="Essays on Some Unsettled Questions of Political Economy", slug="essays-on-some-unsettled-questions-of-political-economy", author_key="john-stuart-mill", year=1844, original_language="en", ebook_id=12004, tags=["economics", "liberalism", "political-economy"], excerpt="Early Mill essays on method, international trade, and unresolved economic disputes."),
    work(title="Essays on Education and Kindred Subjects", slug="essays-on-education-and-kindred-subjects", author_key="herbert-spencer", year=1861, original_language="en", ebook_id=16510, tags=["education", "individualism", "liberalism"], excerpt="Spencer's essays on education, development, and self-formation."),
    work(title="First Principles", slug="first-principles", author_key="herbert-spencer", year=1862, original_language="en", ebook_id=55046, tags=["evolution", "liberalism", "philosophy"], excerpt="Spencer's broad philosophical starting point for his synthetic system."),
    work(title="Illustrations of Universal Progress", slug="illustrations-of-universal-progress", author_key="herbert-spencer", year=1857, original_language="en", ebook_id=39977, tags=["evolution", "liberalism", "social-theory"], excerpt="A set of discussions where Spencer applies evolutionary reasoning across domains."),
    work(title="Essays: Scientific, Political, and Speculative, Vol. 1", slug="spencer-essays-vol-1", author_key="herbert-spencer", year=1858, original_language="en", ebook_id=29869, tags=["liberalism", "politics", "science"], excerpt="The first volume of Spencer's collected essays across science and politics."),
    work(title="Essays: Scientific, Political, and Speculative, Vol. 2", slug="spencer-essays-vol-2", author_key="herbert-spencer", year=1863, original_language="en", ebook_id=53395, tags=["liberalism", "politics", "science"], excerpt="The second volume of Spencer's collected essays across science and politics."),
    work(title="Essays: Scientific, Political, and Speculative, Vol. 3", slug="spencer-essays-vol-3", author_key="herbert-spencer", year=1874, original_language="en", ebook_id=54076, tags=["liberalism", "politics", "science"], excerpt="The third volume of Spencer's collected essays across science and politics."),
    work(title="The Philosophy of Style", slug="the-philosophy-of-style", author_key="herbert-spencer", year=1852, original_language="en", ebook_id=5849, tags=["language", "liberalism", "style"], excerpt="Spencer's well-known essay on clarity, force, and economy in expression."),
    work(title="The Data of Ethics", slug="the-data-of-ethics", author_key="herbert-spencer", year=1879, original_language="en", ebook_id=46129, tags=["ethics", "liberalism", "individualism"], excerpt="Spencer's ethical groundwork for his broader individualist social philosophy."),
    work(title="The Right to Ignore the State", slug="the-right-to-ignore-the-state", author_key="herbert-spencer", year=1851, original_language="en", ebook_id=34649, tags=["individualism", "liberalism", "state"], excerpt="A concise statement of Spencer's anti-paternalist argument about political authority."),
    work(title="The Factors of Organic Evolution", slug="the-factors-of-organic-evolution", author_key="herbert-spencer", year=1887, original_language="en", ebook_id=52801, tags=["evolution", "science", "social-theory"], excerpt="Spencer's treatment of evolutionary causation and biological development."),
    work(title="The Principles of Biology, Volume 1", slug="principles-of-biology-volume-1", author_key="herbert-spencer", year=1864, original_language="en", ebook_id=54612, tags=["biology", "evolution", "science"], excerpt="The first volume of Spencer's large-scale biological synthesis."),
    work(title="The Principles of Biology, Volume 2", slug="principles-of-biology-volume-2", author_key="herbert-spencer", year=1867, original_language="en", ebook_id=67282, tags=["biology", "evolution", "science"], excerpt="The second volume of Spencer's large-scale biological synthesis."),
    work(title="Two Treatises of Government", slug="two-treatises", author_key="john-locke", year=1689, original_language="en", ebook_id=7370, tags=["government", "liberalism", "natural-rights"], excerpt="Locke's classic argument for natural rights, consent, and resistance to arbitrary power."),
    work(title="An Essay Concerning Humane Understanding, Volume 1", slug="essay-concerning-humane-understanding-volume-1", author_key="john-locke", year=1689, original_language="en", ebook_id=10615, tags=["knowledge", "liberalism", "philosophy"], excerpt="The first volume of Locke's foundational inquiry into the origins and limits of human knowledge."),
    work(title="An Essay Concerning Humane Understanding, Volume 2", slug="essay-concerning-humane-understanding-volume-2", author_key="john-locke", year=1689, original_language="en", ebook_id=10616, tags=["knowledge", "liberalism", "philosophy"], excerpt="The second volume of Locke's foundational inquiry into the origins and limits of human knowledge."),
    work(title="An Inquiry into the Nature and Causes of the Wealth of Nations", slug="wealth-of-nations", author_key="adam-smith", year=1776, original_language="en", ebook_id=3300, tags=["economics", "liberalism", "markets"], excerpt="Smith's central work on labor, exchange, institutions, and commercial society."),
    work(title="The Theory of Moral Sentiments", slug="the-theory-of-moral-sentiments", author_key="adam-smith", year=1759, original_language="en", ebook_id=67363, tags=["ethics", "liberalism", "moral-philosophy"], excerpt="Smith's account of sympathy, judgment, and the moral foundations of social life."),
    work(title="The Essays of Adam Smith", slug="the-essays-of-adam-smith", author_key="adam-smith", year=1795, original_language="en", ebook_id=58559, tags=["economics", "liberalism", "moral-philosophy"], excerpt="A collection of Smith's shorter writings and lectures beyond The Wealth of Nations."),
    work(title="Dialogues Concerning Natural Religion", slug="dialogues-concerning-natural-religion", author_key="david-hume", year=1779, original_language="en", ebook_id=4583, tags=["liberalism", "philosophy", "skepticism"], excerpt="Hume's dialogical treatment of religion, design, and the limits of inference."),
    work(title="Enquiry Concerning Human Understanding", slug="enquiry-concerning-human-understanding", author_key="david-hume", year=1748, original_language="en", ebook_id=9662, tags=["knowledge", "liberalism", "skepticism"], excerpt="Hume's classic statement of empiricism, causation, and the limits of certainty."),
    work(title="Enquiry Concerning the Principles of Morals", slug="enquiry-concerning-the-principles-of-morals", author_key="david-hume", year=1751, original_language="en", ebook_id=4320, tags=["ethics", "liberalism", "moral-philosophy"], excerpt="Hume's account of virtue, utility, sentiment, and moral judgment."),
    work(title="Essays", slug="essays-by-david-hume", author_key="david-hume", year=1741, original_language="en", ebook_id=36120, tags=["essays", "liberalism", "politics"], excerpt="A set of Hume essays that connect commercial society, manners, and politics."),
    work(title="Hume's Political Discourses", slug="humes-political-discourses", author_key="david-hume", year=1752, original_language="en", ebook_id=59792, tags=["economics", "liberalism", "politics"], excerpt="Hume's essays on commerce, money, population, and constitutional questions."),
    work(title="Treatise of Human Nature", slug="treatise-of-human-nature", author_key="david-hume", year=1739, original_language="en", ebook_id=4705, tags=["liberalism", "philosophy", "skepticism"], excerpt="Hume's early major work on understanding, passions, and morals."),
    work(title="History of England in Three Volumes, Vol. I, Part A", slug="history-of-england-vol-1-part-a", author_key="david-hume", year=1754, original_language="en", ebook_id=19211, tags=["history", "institutions", "liberalism"], excerpt="The opening part of Hume's large-scale history of England."),
    work(title="History of England in Three Volumes, Vol. I, Part B", slug="history-of-england-vol-1-part-b", author_key="david-hume", year=1754, original_language="en", ebook_id=19212, tags=["history", "institutions", "liberalism"], excerpt="The second part of Hume's large-scale history of England."),
    work(title="History of England in Three Volumes, Vol. I, Part C", slug="history-of-england-vol-1-part-c", author_key="david-hume", year=1754, original_language="en", ebook_id=19213, tags=["history", "institutions", "liberalism"], excerpt="The third part of Hume's large-scale history of England."),
    work(title="History of England in Three Volumes, Vol. I, Part D", slug="history-of-england-vol-1-part-d", author_key="david-hume", year=1754, original_language="en", ebook_id=19214, tags=["history", "institutions", "liberalism"], excerpt="The fourth part of Hume's large-scale history of England."),
    work(title="History of England in Three Volumes, Vol. I, Part E", slug="history-of-england-vol-1-part-e", author_key="david-hume", year=1754, original_language="en", ebook_id=19215, tags=["history", "institutions", "liberalism"], excerpt="The fifth part of Hume's large-scale history of England."),
    work(title="History of England in Three Volumes, Vol. I, Part F", slug="history-of-england-vol-1-part-f", author_key="david-hume", year=1754, original_language="en", ebook_id=19216, tags=["history", "institutions", "liberalism"], excerpt="The sixth part of Hume's large-scale history of England."),
    work(title="Democracy in America", slug="democracy-in-america", author_key="alexis-de-tocqueville", year=1835, original_language="fr", ebook_id=815, tags=["democracy", "institutions", "liberalism"], excerpt="The first English volume of Tocqueville's classic on democracy and civil society."),
    work(title="Democracy in America, Volume 2", slug="democracy-in-america-volume-2", author_key="alexis-de-tocqueville", year=1840, original_language="fr", ebook_id=816, tags=["democracy", "institutions", "liberalism"], excerpt="The second English volume of Tocqueville's classic on democracy and civil society."),
    work(title="De la Democratie en Amerique, tome premier", slug="de-la-democratie-en-amerique-tome-1", author_key="alexis-de-tocqueville", year=1835, original_language="fr", ebook_id=30513, tags=["america", "democracy", "institutions"], excerpt="The first French tome of Tocqueville's study of democracy in America."),
    work(title="De la Democratie en Amerique, tome deuxieme", slug="de-la-democratie-en-amerique-tome-2", author_key="alexis-de-tocqueville", year=1835, original_language="fr", ebook_id=30514, tags=["america", "democracy", "institutions"], excerpt="The second French tome of Tocqueville's study of democracy in America."),
    work(title="De la Democratie en Amerique, tome troisieme", slug="de-la-democratie-en-amerique-tome-3", author_key="alexis-de-tocqueville", year=1840, original_language="fr", ebook_id=30515, tags=["america", "centralization", "democracy"], excerpt="The third French tome of Tocqueville's study of democracy in America."),
    work(title="De la Democratie en Amerique, tome quatrieme", slug="de-la-democratie-en-amerique-tome-4", author_key="alexis-de-tocqueville", year=1840, original_language="fr", ebook_id=30516, tags=["america", "centralization", "democracy"], excerpt="The fourth French tome of Tocqueville's study of democracy in America."),
    work(title="State of Society in France Before the Revolution of 1789", slug="state-of-society-in-france-before-the-revolution-of-1789", author_key="alexis-de-tocqueville", year=1856, original_language="fr", ebook_id=54187, tags=["france", "history", "institutions"], excerpt="Tocqueville's prehistory of the centralizing tendencies that shaped the French Revolution."),
    work(title="Ancien Regime et la Revolution", slug="ancien-regime-et-la-revolution", author_key="alexis-de-tocqueville", year=1856, original_language="fr", ebook_id=54339, tags=["france", "history", "institutions"], excerpt="The French text of Tocqueville's study of the old regime and revolutionary continuity."),
    work(title="The Road to Serfdom", slug="road-to-serfdom", author_key="f-a-hayek", year=1944, original_language="en", source_url="https://press.uchicago.edu/ucp/books/book/chicago/R/bo5984308.html", source_text_url="", tags=["liberalism", "central-planning", "state"], excerpt="A chapter-level guide to Hayek's critique of comprehensive planning and its political consequences.", mode="guide"),
]


def build_catalog() -> dict[str, list[dict[str, object]]]:
    authors = deepcopy(AUTHORS)
    works = deepcopy(WORKS)
    authors_by_key = {author["key"]: author for author in authors}
    for work_entry in works:
        author = authors_by_key[work_entry["author_key"]]
        work_entry["author"] = author["name"]
        work_entry["subtitle"] = author["name"]
        work_entry["search_tags"] = ", ".join(work_entry["tags"])
    return {"authors": authors, "works": works}
